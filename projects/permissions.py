from rest_framework import permissions

from contributors.models import Contributor

from softdesk.permissions import IsAuthor, IsContributor


class IsProjectAuthor(IsAuthor):
    """Custom permission to only allow owners of a project to edit or delete it."""

    message = "Must be the author of the project !"

    def has_object_permission(self, request, view, obj):
        try:
            contributor = Contributor.objects.get(author_user=request.user, project=obj)
        except Contributor.DoesNotExist:
            return False
        if contributor.permission == "Manager":
            return True
        elif contributor.permission == "Read":
            return request.method in permissions.SAFE_METHODS


class IsProjectContributor(IsContributor):
    """Custom permission to only allow contributors of a project to view it."""

    message = "Must be a contributor !"
