from rest_framework import viewsets, permissions

from issues.models import Issue
from softdesk.permissions import IsAuthor, IsContributor

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows comments to be viewed or edited."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthor,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        issue_pk = Issue.objects.get(pk=self.kwargs["issue_pk"])
        serializer.save(issue=issue_pk)

    def get_queryset(self, **kwargs):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])
