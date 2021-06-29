from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

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
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, password):
        if validate_password(password) is None:
            return make_password(password)
