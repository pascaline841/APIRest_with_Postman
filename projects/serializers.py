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

    def create(self, validated_data):
        new_project = Project.objects.create(**validated_data)
        author = self.context["request"].user
        new_project.author_user = author
        contributor = Contributor.objects.create(
            author_user=author,
            project=new_project,
            permission="Manager",
            role="Manager",
        )
        new_project.contributors.append(contributor)
        new_project.save()
        return new_project
