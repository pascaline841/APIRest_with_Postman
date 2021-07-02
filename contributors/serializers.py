from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    author_user = serializers.ReadOnlyField(source="author_user.username")

    class Meta:
        model = Contributor
        fields = "__all__"
        read_only_fields = ["project"]
