from rest_framework import viewsets, permissions

from .models import Comment
from .permissions import CommentPermission
from .serializers import CommentSerializer

from issues.models import Issue


class CommentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows comments to be viewed or edited."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated, CommentPermission]

    def perform_create(self, serializer, **kwargs):
        issue_pk = Issue.objects.get(pk=self.kwargs["issue_pk"])
        serializer.save(issue=issue_pk)

    def get_queryset(self, **kwargs):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])
