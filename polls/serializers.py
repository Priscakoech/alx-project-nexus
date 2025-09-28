from rest_framework import serializers
from django.utils import timezone
from .models import Poll, Option, Vote

class OptionSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Option
        fields = ("id", "text", "votes_count")

    def get_votes_count(self, obj):
        # counts related Vote objects; uses related_name 'votes' on Vote.option
        return obj.vote_records.count()


class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=True)
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Poll
        fields = ("id", "question", "created_by", "created_at", "expiry_date", "options")
        read_only_fields = ("created_by", "created_at")

    def validate_expiry_date(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("expiry_date cannot be in the past")
        return value

    def create(self, validated_data):
        options_data = validated_data.pop("options")
        poll = Poll.objects.create(**validated_data)
        for option in options_data:
            Option.objects.create(poll=poll, **option)
        return poll

    def update(self, instance, validated_data):
        # Only update question & expiry_date, not options
        instance.question = validated_data.get("question", instance.question)
        instance.expiry_date = validated_data.get("expiry_date", instance.expiry_date)
        instance.save()
        return instance


class VoteSerializer(serializers.ModelSerializer):
    voted_by = serializers.ReadOnlyField(source="voted_by.username")

    class Meta:
        model = Vote
        fields = ("id", "option", "voted_by", "ip_address", "created_at")
        read_only_fields = ("voted_by", "created_at", "ip_address")

    def validate(self, attrs):
        """
        Prevent duplicate voting:
        - If user authenticated: ensure they haven't voted on this poll.
        - If anonymous: ensure the IP hasn't voted on this poll.
        """
        request = self.context.get("request", None)
        option = attrs.get("option")

        if option is None:
            raise serializers.ValidationError("option is required")

        poll = option.poll
        user = None

        # Only check duplicates if we actually have a request (skip in schema gen)
        if request and hasattr(request, "user"):
            user = request.user if request.user.is_authenticated else None

            if user and Vote.objects.filter(option__poll=poll, voted_by=user).exists():
                raise serializers.ValidationError("User has already voted in this poll.")
            elif not user:
                xff = request.META.get("HTTP_X_FORWARDED_FOR")
                ip = (xff.split(",")[0].strip() if xff else request.META.get("REMOTE_ADDR"))
                if ip and Vote.objects.filter(option__poll=poll, ip_address=ip).exists():
                    raise serializers.ValidationError("This IP has already voted in this poll.")
                attrs["ip_address"] = ip

        return attrs

    def create(self, validated_data):
        request = self.context.get("request", None)
        user = None
        if request and hasattr(request, "user") and request.user.is_authenticated:
            user = request.user

        ip = validated_data.pop("ip_address", None)
        return Vote.objects.create(voted_by=user, ip_address=ip, **validated_data)
