from django.conf import settings

from django.db import models

from projects.models import Project


class Contributor(models.Model):

    PERMISSION_CHOICES = [("Manager", "Manager"), ("Read", "Read")]

    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, blank=True, null=True
    )
    permission = models.CharField(
        max_length=7, choices=PERMISSION_CHOICES, default="Read"
    )
    role = models.CharField(max_length=128)

    def __str__(self):
        return f"Contributor : {self.author_user} / {self.project.title}"
