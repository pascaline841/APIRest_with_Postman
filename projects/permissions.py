from rest_framework import permissions

from contributors.models import Contributor


class ProjectPermission(permissions.BasePermission):
    """
    Permission for all to view his project or create a new one.
    Permission for author to modificate/delete project.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project_id=obj
            )
        except Contributor.DoesNotExist:
            return False

        if contributor.permission == "Manager":
            return True
        elif contributor.permission == "Read":
            return request.method in permissions.SAFE_METHODS
