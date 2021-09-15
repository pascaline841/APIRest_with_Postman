from rest_framework import serializers

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source="project.title")
    author = serializers.ReadOnlyField(source="author.username")
    assignee_user = serializers.ReadOnlyField(source="assignee_user.username")

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author", "project", "assignee_user"]
