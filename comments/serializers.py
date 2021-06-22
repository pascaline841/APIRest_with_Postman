from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_user_id = serializers.ReadOnlyField(source="author_user_id.username")
    issue_id = serializers.ReadOnlyField(source="issue_id.title")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author_user_id", "issue_id"]

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        # temporary
        user = get_user_model().objects.all().first()
        # user = self.context["request"].user
        comment.author_user_id = user
        comment.save()
        return comment
