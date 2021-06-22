from django.contrib.auth import get_user_model

from rest_framework import serializers

from contributors.models import Contributor

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author_user = serializers.ReadOnlyField(source="author_user.username")

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author_user"]

    def __str__(self):
        return f"Project: {self.title}, {self.description}, {self.type}, {self.author_user}"

    def create(self, validated_data):
        new_project = Project.objects.create(**validated_data)
        # temporary
        username = get_user_model().objects.all().first()
        # user = self.context["request"].user
        new_project.author_user = username
        new_project.save()
        Contributor.objects.create(
            user=username,
            project=new_project,
            permission="Manager",
            role="Manager",
        )
        return new_project
