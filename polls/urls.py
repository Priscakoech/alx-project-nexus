from django.urls import path
from .views import PollListCreateView, PollDetailView, VoteView, PollResultsView

urlpatterns = [
    path("polls/", PollListCreateView.as_view(), name="poll-list-create"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll-detail"),
    path("polls/<int:poll_id>/vote/<int:option_id>/", VoteView.as_view(), name="vote"),
    path("polls/<int:poll_id>/results/", PollResultsView.as_view(), name="poll-results"),
]
