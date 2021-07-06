from rest_framework import permissions

from contributors.models import Contributor


class ProjectPermission(permissions.BasePermission):
    message = "Must be the author or a manager of the project !"

    def has_object_permission(self, request, view, obj):
        try:
            manager = Contributor.objects.get(author_user=request.user, project=obj)
        except Contributor.DoesNotExist:
            return False
        if manager.permission == "Manager" or obj.author_user == request.user:
            return True
        else:
            return request.method in permissions.SAFE_METHODS
