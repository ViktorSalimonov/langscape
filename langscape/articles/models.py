# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


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
