from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.question


class Option(models.Model):
    poll = models.ForeignKey(Poll, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text} ({self.poll.question})"

class Vote(models.Model):
    option = models.ForeignKey(Option, related_name="vote_records", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents same user voting twice on the same poll
        unique_together = ("user", "option")
        # If using IP address instead of user accounts
        constraints = [
            models.UniqueConstraint(
                fields=["ip_address", "option"], name="unique_vote_per_ip_option"
            )
        ]

    def __str__(self):
        voter = self.user.username if self.user else self.ip_address
        return f"Vote by {voter} on {self.option.text}"
