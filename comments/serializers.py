from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_user = serializers.ReadOnlyField(source="author_user.username")
    issue = serializers.ReadOnlyField(source="issue.title")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author_user", "issue"]

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        # temporary
        user = get_user_model().objects.all().first()
        # user = self.context["request"].user
        comment.author_user = user
        comment.save()
        return comment
