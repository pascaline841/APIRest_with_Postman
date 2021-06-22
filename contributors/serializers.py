from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Contributor
        fields = "__all__"
        read_only_fields = ["project"]
