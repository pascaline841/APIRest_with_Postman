from django.conf import settings

from django.db import models

from projects.models import Project


class Contributor(models.Model):

    username = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributor",
        blank=True,
        null=True,
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="contributors",
        blank=True,
        null=True,
    )
    role = models.CharField(max_length=128)

    def __str__(self):
        return f"PROJECT : {self.project.title}, CONTRIBUTOR : {self.username}"
