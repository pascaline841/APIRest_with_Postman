from rest_framework import viewsets, permissions

from projects.models import Project

from .models import Contributor
from .permissions import ContributorPermission
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    """API endpoint that contributors users to be viewed or edited."""

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer, **kwargs):
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk)

    def get_queryset(self, **kwargs):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])
