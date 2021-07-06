from django.contrib.auth import get_user_model

from rest_framework import serializers

from contributors.models import Contributor

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["author"]

    def create(self, validated_data):
        """
        Function to create a new project,
        the author will be  a manager and the first contributor.
        """

        new_project = Project.objects.create(**validated_data)
        author = self.context["request"].user
        new_project.author = author
        contributor = Contributor.objects.create(
            author=author,
            project=new_project,
            permission="Manager",
            role="Manager",
        )
        new_project.contributors.append(contributor)
        new_project.save()
        return new_project
