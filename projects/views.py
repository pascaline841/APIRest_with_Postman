from rest_framework import permissions, viewsets

from .models import Project
from .permissions import ProjectPermission
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, ProjectPermission]

    def getqueryset(self, *args, **kwargs):
        return Project.objects.filter(author_user=self.request.user)
