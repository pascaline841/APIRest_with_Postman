from rest_framework import permissions


from softdesk.permissions import IsAuthor, IsContributor

from contributors.models import Contributor


class IsProjectAuthor(IsAuthor):
    """Custom permission to only allow owners of a project to edit or delete it."""

    message = "Must be the author or a manager of the project to edit or delete it!"
    """
    def has_object_permission(self, request, view, obj):
        try:
            contributor = Contributor.objects.get(author_user=request.user, project=obj)
        except Contributor.DoesNotExist:
            return False
        return contributor.permission == "Manager" or obj.author_user == request.user
    """


class IsProjectContributor(IsContributor):
    """Custom permission to only allow contributors of a project to view it."""

    message = "Must be a contributor of the project to view it !"
