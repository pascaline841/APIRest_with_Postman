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
        The author will be a manager and the first contributor.
        """
        new_project = Project.objects.create(**validated_data)
        new_project.author = self.context["request"].user
        new_project.save()
        Contributor.objects.create(
            username=self.context["request"].user,
            project=new_project,
            role="Manager",
        )
        return new_project
