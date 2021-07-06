from contributors.models import Contributor
from issues.models import Issue
from softdesk.permissions import IsAuthor, IsContributor


class IsCommentAuthor(IsAuthor):
    """Custom permission to only allow author of a comment to edit or delete it."""

    message = "Must be the author of the comment !"

    def has_permission(self, request, view):
        issue_pk = view.kwargs.get("issue_pk")
        try:
            issue = Issue.objects.get(id=issue_pk)
        except Issue.DoesNotExist:
            return False
        assignee = issue.assignee_user


class IsCommentContributor(IsContributor):
    """Custom permission to only allow contributors of the project to create or view the comments."""

    def has_permission(self, request, view):
        """Custom permission to only allow contributors of the project to view the comments."""
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        return contributor


""" 
    def has_permission(self, request, view):

        issue_pk = view.kwargs.get("issue_pk")
        try:
            issue = Issue.objects.get(id=issue_pk)
        except Issue.DoesNotExist:
            return False
        try:
            contributor = Contributor.objects.get(
                contributor=request.user, project=issue.project
            )
        except Contributor.DoesNotExist:
            return False
        return contributor or issue.author_user == request.user
"""
