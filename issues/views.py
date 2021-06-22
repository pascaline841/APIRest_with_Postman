from rest_framework import viewsets, permissions

from projects.models import Project

from .models import Issue
from .permissions import IssuePermission
from .serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """API endpoint that allows issues to be viewed or edited."""

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    # permission_classes = [permissions.IsAuthenticated, IssuePermission]

    def perform_create(self, serializer, **kwargs):
        project_pk = self.kwargs["project_pk"]
        project = Project.objects.get(pk=project_pk)
        serializer.save(project_id=project)

    def get_queryset(self, **kwargs):
        project_pk = self.kwargs["project_pk"]
        return Issue.objects.filter(project_id=project_pk)
    
