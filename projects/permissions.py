from rest_framework import permissions


class ProjectPermission(permissions.BasePermission):
    """Custom permission to only allow owners of an project to edit it."""

    pass
