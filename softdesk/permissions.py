from rest_framework import permissions

from contributors.models import Contributor


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author_user == request.user:
            return True


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        return True


class IsManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        project_pk = view.kwargs.get("project_pk")
        try:
            manager = Contributor.objects.get(
                author_user=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        return manager.permission == "Manager"
