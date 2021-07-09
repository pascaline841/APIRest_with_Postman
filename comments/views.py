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
        """Create a comment from a specific issue."""
        issue_pk = Issue.objects.get(pk=self.kwargs["issue_pk"])
        author_comment = self.request.user
        serializer.save(issue=issue_pk, author=author_comment)

    def get_queryset(self, **kwargs):
        """Get and display the list of comments from a specific issue."""
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])
