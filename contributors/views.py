from rest_framework import viewsets, permissions

from projects.models import Project
from softdesk.permissions import IsAuthorOrManager, IsContributor

from .models import Contributor
from .serializers import ContributorSerializer


class ContributorViewSet(viewsets.ModelViewSet):
    """API endpoint that contributors users to be viewed or edited."""

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrManager,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Create a contributor from a specific project."""
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk)

    def get_queryset(self, **kwargs):
        """Get and display the list of contributors from a specific project."""
        return Contributor.objects.filter(project=self.kwargs["project_pk"])
