from rest_framework import permissions, viewsets

from contributors.models import Contributor
from softdesk.permissions import IsAuthor
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthor,
    ]

    def get_queryset(self, *args, **kwargs):
        """
        Get and display the list of the project where
        the user is the author or contributor.
        """
        contributors = Contributor.objects.filter(username=self.request.user)
        projects = [contributor.project.id for contributor in contributors]
        return Project.objects.filter(id__in=projects)
