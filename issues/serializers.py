from rest_framework import serializers

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source="project.title")
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author", "project"]

    def create(self, validated_data):
        """Function to create and save an issue from a project."""
        issue = Issue.objects.create(**validated_data)
        issue.author = self.context["request"].user
        issue.save()
        return issue
