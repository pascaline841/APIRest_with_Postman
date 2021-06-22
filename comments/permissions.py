from rest_framework import permissions


class CommentPermission(permissions.BasePermission):
    """
    Custom permission to only allow contributors of an project
    to access to comment project.
    """
    pass