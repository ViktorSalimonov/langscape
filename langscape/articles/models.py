# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuid_lib

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    editor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username


class Article(TimeStampedModel):
    DIFFICULTY_ANY = 'any'
    DIFFICULTY_BEGINNER = 'beg'
    DIFFICULTY_MEDIUM = 'med'
    DIFFICULTY_ADVANCED = 'adv'

    DIFFICULTY_CHOICES = (
        (DIFFICULTY_ANY, 'Any'),
        (DIFFICULTY_BEGINNER, 'Beginner'),
        (DIFFICULTY_MEDIUM, 'Medium'),
        (DIFFICULTY_ADVANCED, 'Advanced')
    )
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=3,
                                  choices=DIFFICULTY_CHOICES,
                                  default=DIFFICULTY_ANY)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.objects.pk})

    def __unicode__(self):
        return self.title


class Comment(TimeStampedModel):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name="comments")
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __unicode__(self):
        return self.content
