from rest_framework import viewsets, permissions

from projects.models import Project

from .models import Contributor
from .permissions import ContributorPermission
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    """API endpoint that contributors users to be viewed or edited."""

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    # permission_classes = [permissions.IsAuthenticated, ContributorPermission]

    def perform_create(self, serializer, **kwargs):
        project_pk = self.kwargs["project_pk"]
        project = Project.objects.get(pk=project_pk)
        serializer.save(project_id=project)

    def get_queryset(self, **kwargs):
        project_pk = self.kwargs["project_pk"]
        return Contributor.objects.filter(project_id=project_pk)
