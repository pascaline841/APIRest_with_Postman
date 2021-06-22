from django.conf import settings
from django.db import models

from projects.models import Project


class Contributor(models.Model):

    PERMISSION_CHOICES = [("Manager", "Manager"), ("Read", "Read")]

    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    project_id = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, blank=True, null=True
    )
    permission = models.CharField(
        max_length=10, choices=PERMISSION_CHOICES, default="Read"
    )
    role = models.CharField(max_length=128)
