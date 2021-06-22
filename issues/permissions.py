from rest_framework import permissions


class IssuePermission(permissions.BasePermission):
    """
    Custom permission to only allow contributors of an project
    to access to issues' project.
    """
    pass