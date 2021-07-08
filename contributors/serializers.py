from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source="project.title")
    username = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(), fields=["username"]
            )
        ]
        model = Contributor
        fields = "__all__"

    def create(self, validated_data):
        """Function to create and save a contributor from a project."""
        contributor = Contributor.objects.create(**validated_data)
        contributor.save()
        return contributor
