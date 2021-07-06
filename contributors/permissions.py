from rest_framework import permissions

from .models import Contributor


class ContributorPermission(permissions.BasePermission):

    message = "Must be a contributor of the project to view it !"

    def has_permission(self, request, view):
        """
        Custom permission to only allow contributors of a project to view the list of
        the contributors of a project.
        """
        project_pk = view.kwargs.get("project_pk")
        try:
            contributor = Contributor.objects.get(
                author_user=request.user, project=project_pk
            )
        except Contributor.DoesNotExist:
            return False
        if contributor.permission in ["Manager", "Read"]:
            return True

    def has_object_permission(self, request, view, obj):
        """
        Custom permission to only allow managers of a project to create, edit or delete
        a contributor of a project.
        """
        try:
            contributor = Contributor.objects.get(user=request.user, project_id=obj)
        except Contributor.DoesNotExist:
            return False
        return contributor.permission == "Manager"
