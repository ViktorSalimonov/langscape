import uuid as uuid_lib

from django.contrib.auth.models import User
from django.db import models


class TimeStampedModel(models.Model):
    """Extend standard model."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Article(TimeStampedModel):
    """Article model."""

    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title
