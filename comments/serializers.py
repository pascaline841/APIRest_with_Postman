from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    issue = serializers.ReadOnlyField(source="issue.title")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "issue"]

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        author = self.context["request"].user
        comment.author = author
        comment.save()
        return comment
