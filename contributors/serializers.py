from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    project = serializers.ReadOnlyField(source="project.title")

    class Meta:
        model = Contributor
        fields = "__all__"
        read_only_fields = ["author", "project"]

    def create(self, validated_data):
        """Function to create and save a contributor from a project."""
        contributor = Contributor.objects.create(**validated_data)
        contributor.save()
        return contributor
