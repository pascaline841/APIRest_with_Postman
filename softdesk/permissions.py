from rest_framework import permissions

from contributors.models import Contributor


class IsAuthor(permissions.BasePermission):
    """Custom permission to only allow author of an object to edit or delete it."""

    message = "Must be the author !"

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        else:
            return request.method in permissions.SAFE_METHODS


class IsContributor(permissions.BasePermission):
    """Custom permission to only allow contributors of a project to view it."""

    message = "Must be a contributor of the project !"

    def has_permission(self, request, view):
        project_pk = view.kwargs.get("project_pk")
        try:
            Contributor.objects.get(username_id=request.user, project=project_pk)
        except Contributor.DoesNotExist:
            return False
        return True


class IsAuthorOrManager(permissions.BasePermission):
    """Custom permission to only allow author or managers to edit or delete it."""

    message = "Must be the author or a manager of the project !"

    def has_object_permission(self, request, view, obj):
        project_pk = view.kwargs.get("project_pk")
        try:
            manager = Contributor.objects.get(
                username_id=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        if manager.permission == "Manager" or obj.author == request.user:
            return True
        else:
            return request.method in permissions.SAFE_METHODS
