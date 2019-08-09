from django import forms

from langscape.articles.models import Comment
from langscape.articles.validators import validate_comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].validators.append(validate_comment)

    class Meta:
        model = Comment
        fields = (
            'content',
        )
