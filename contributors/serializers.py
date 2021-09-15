from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(), fields=["username", "project"]
            )
        ]
        model = Contributor
        fields = "__all__"
