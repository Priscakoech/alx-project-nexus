from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Poll, Option, Vote
from .serializers import PollSerializer, OptionSerializer, VoteSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated


# 1. List all polls OR create a new poll
class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all().order_by("-created_at")
    serializer_class = PollSerializer
    
    # only logged in users can create polls, but listing polls is public
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return []


# 2. Get poll details
class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


# 3. Vote on an option
class VoteView(APIView):
    def post(self, request, poll_id, option_id):
        poll = get_object_or_404(Poll, id=poll_id)
        option = get_object_or_404(Option, id=option_id, poll=poll)

        # Check if poll is expired
        if poll.expiry_date and poll.expiry_date < timezone.now():
            return Response({"error": "Poll has expired"}, status=status.HTTP_400_BAD_REQUEST)

        # Prevent duplicate votes by user or IP
        user = request.user if request.user.is_authenticated else None
        ip_address = request.META.get("REMOTE_ADDR")

        if Vote.objects.filter(option__poll=poll, user=user, ip_address=ip_address).exists():
            return Response({"error": "You have already voted"}, status=status.HTTP_400_BAD_REQUEST)

        # Create vote
        vote = Vote.objects.create(option=option, user=user, ip_address=ip_address)
        return Response(VoteSerializer(vote).data, status=status.HTTP_201_CREATED)


# 4. Get results (options + vote counts)
class PollResultsView(APIView):
    def get(self, request, poll_id):
        poll = get_object_or_404(Poll, id=poll_id)
        options = Option.objects.filter(poll=poll)
        serializer = OptionSerializer(options, many=True)
        return Response({
            "poll": poll.question,
            "results": serializer.data
        })
        

