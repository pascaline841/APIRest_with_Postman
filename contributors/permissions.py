from rest_framework import permissions

from .models import Contributor


class ContributorPermission(permissions.BasePermission):
    """Custom permission to only allow contributors of an object to edit it."""

    def has_permission(self, request, view):
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project_id=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        if contributor.permission in ["Manager", "Read"]:
            return True

    def has_object_permission(self, request, view, obj):
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project_id=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        if contributor.permission == "Manager":
            return request.method in ["DELETE"]
        elif contributor.permission == "Read":
            if request.user == obj.author_user:
                return True
            else:
                return request.method in permissions.SAFE_METHODS
