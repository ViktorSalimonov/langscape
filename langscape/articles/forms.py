# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Article
from .validators import validate_article


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators.append(validate_article)

    class Meta:
        model = Article
        fields = (
            'title',
            'difficulty',
            'text'
        )
