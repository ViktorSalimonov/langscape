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
    __DIFFICULTY_ANY = 'any'
    __DIFFICULTY_BEGINNER = 'beg'
    __DIFFICULTY_MEDIUM = 'med'
    __DIFFICULTY_ADVANCED = 'adv'

    DIFFICULTY_CHOICES = (
        (__DIFFICULTY_ANY, 'Any'),
        (__DIFFICULTY_BEGINNER, 'Beginner'),
        (__DIFFICULTY_MEDIUM, 'Medium'),
        (__DIFFICULTY_ADVANCED, 'Advanced')
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    title = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=3, choices=DIFFICULTY_CHOICES, default=__DIFFICULTY_ANY)
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.objects.pk})

    def __unicode__(self):
        return self.title


class Comment(TimeStampedModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __unicode__(self):
        return self.content
