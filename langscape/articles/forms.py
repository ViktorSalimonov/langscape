# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Comment
from .validators import validate_comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].validators.append(validate_comment)

    class Meta:
        model = Comment
        fields = (
            'content',
        )
