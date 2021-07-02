from contributors.models import Contributor
from softdesk.permissions import IsAuthor, IsContributor


class IsCommentAuthor(IsAuthor):
    """Custom permission to only allow author of a comment to edit or delete it."""

    message = "Must be the author of the comment !"


class IsCommentContributor(IsContributor):
    """Custom permission to only allow contributors of a project to view the comments."""

    def has_object_permission(self, request, view, obj):
        return request.user in [*obj.project.contributors.all(), obj.user]

    def has_permission(self, request, view):
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        if contributor.permission in ["Manager", "Read"]:
            return True
