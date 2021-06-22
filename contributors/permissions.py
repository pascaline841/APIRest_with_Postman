from rest_framework import permissions


class ContributorPermission(permissions.BasePermission):
    """Custom permission to only allow contributors of an object to edit it."""

    pass