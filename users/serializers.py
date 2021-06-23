from django.contrib.auth.models import User

from rest_framework import serializers

from rest_framework_simplejwt.serializers import PasswordField


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):
        return User.objects.create(**validated_data)
