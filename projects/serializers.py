from django.contrib.auth import get_user_model

from rest_framework import serializers

from contributors.models import Contributor

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author_user_id = serializers.ReadOnlyField(source="author_user_id.username")

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author_user_id"]

    def __str__(self):
        return f"Project: {self.title}, {self.description}, {self.type}, {self.author_user_id}"

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        # temporary
        user = get_user_model().objects.all().first()
        # user = self.context["request"].user
        project.author_user_id = user
        project.save()
        Contributor.objects.create(
            user_id=user,
            project_id=project,
            permission="Manager",
            role="Manager",
        )
        return project
