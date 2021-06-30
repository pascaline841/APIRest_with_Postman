from django.conf import settings

from django.db import models


class Project(models.Model):

    TYPE_CHOICES = [
        ("back-end", "back-end"),
        ("front-end", "front-end"),
        ("iOS", "iOS"),
        ("Android", "Android"),
    ]
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="back-end")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
