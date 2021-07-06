from rest_framework import permissions, viewsets

from contributors.models import Contributor

from .models import Project
from .serializers import ProjectSerializer
from .permissions import ProjectPermission


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        ProjectPermission,
    ]

    def get_queryset(self, *args, **kwargs):
        contributors = Contributor.objects.filter(author=self.request.user)
        projects = [contributor.project.id for contributor in contributors]
        return Project.objects.filter(id__in=projects)
