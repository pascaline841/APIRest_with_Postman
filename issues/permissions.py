from contributors.models import Contributor
from softdesk.permissions import IsAuthor, IsContributor


class IsIssueAuthor(IsAuthor):
    """Custom permission to only allow author of an issue to edit or delete it."""

    message = "Must be the author of the issue to edit it !"

    '''
    def has_object_permission(self, request, view, obj):
        """Custom permission to only allow manager of a project to create an issue."""
        try:
            contributor = Contributor.objects.get(author_user=request.user, project=obj)
        except Contributor.DoesNotExist:
            return False
        return contributor.permission == "Manager" or obj.author_user == request.user
    '''


class IsIssueContributor(IsContributor):

    message = "Must be a contributor of the project to view the issues !"

    def has_permission(self, request, view):
        """Custom permission to only allow contributors of a project to view a issue."""
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        return contributor
