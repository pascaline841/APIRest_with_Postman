from django.conf import settings
from django.db import models

from issues.models import Issue


class Comment(models.Model):

    comment = models.CharField(max_length=128)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, blank=True, null=True
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment : {self.comment}"
