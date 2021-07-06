from rest_framework import viewsets, permissions

from projects.models import Project
from softdesk.permissions import IsAuthor, IsContributor, IsManager

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
        IsManager,
    ]

    def perform_create(self, serializer, **kwargs):
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk)

    def get_queryset(self, **kwargs):
        return Issue.objects.filter(project=self.kwargs["project_pk"])
