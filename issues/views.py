from rest_framework import viewsets, permissions

from projects.models import Project
from softdesk.permissions import IsAuthor, IsContributor

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """API endpoint that allows issues to be viewed or edited."""

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthor,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Create an issue from a specific project."""
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk, author=self.request.user)

    def get_queryset(self, **kwargs):
        """Get and display the list of issues from a specific project."""
        return Issue.objects.filter(project=self.kwargs["project_pk"])
