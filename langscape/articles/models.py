# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    is_gold = models.BooleanField(default=False)


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
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=3,
                                  choices=DIFFICULTY_CHOICES,
                                  default=DIFFICULTY_ANY)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.objects.pk})
