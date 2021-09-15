from rest_framework import viewsets, permissions
from rest_framework.response import Response
from projects.models import Project
from softdesk.permissions import IsContributor

from .models import Contributor
from .serializers import ContributorSerializer
from rest_framework.response import Response


class ContributorViewSet(viewsets.ModelViewSet):
    """API endpoint that contributors users to be viewed or edited."""

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsContributor,
    ]

    def perform_create(self, serializer, **kwargs):
        """Create a contributor from a specific project."""
        project_pk = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project_pk)

    def get_queryset(self, **kwargs):
        """Get and display the list of contributors from a specific project."""
        return Contributor.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        """Create a contributor without the need to specify the project."""
        datas = request.data.copy()
        datas.__setitem__("project", self.kwargs["project_pk"])
        serializer = self.get_serializer(data=datas)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
