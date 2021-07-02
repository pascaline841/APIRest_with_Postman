from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author_user == request.user


class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
