from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from contributors.models import Contributor

from .models import Project
from .serializers import ProjectSerializer
from .permissions import ProjectPermission


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows projects to be viewed or edited."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated, ProjectPermission]

    def getqueryset(self, *args, **kwargs):
        return Project.objects.filter(author_user=self.request.user)
