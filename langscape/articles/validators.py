from django.core.exceptions import ValidationError


def validate_article(value):
    if len(value) < 3:
        message = "Length of the title must be longer"
        raise ValidationError(message)
