from rest_framework import permissions

from contributors.models import Contributor


class ProjectPermission(permissions.BasePermission):
    """Custom permission to only allow owners of an project to edit it."""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        try:
            contributor = Contributor.objects.get(user=request.user, project=obj)
        except Contributor.DoesNotExist:
            return False
        if contributor.permission == "Manager":
            return True
        elif contributor.permission == "Read":
            return request.method in permissions.SAFE_METHODS
