from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    project_id = serializers.ReadOnlyField(source="project_id.title")
    author_user_id = serializers.ReadOnlyField(source="author_user_id.username")

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author_user_id", "project_id"]

    def create(self, validated_data):
        issue = Issue.objects.create(**validated_data)
        # temporary
        user = get_user_model().objects.all().first()
        # user = self.context["request"].user
        issue.author_user_id = user
        issue.save()
        return issue
