from django.core.exceptions import ValidationError


def validate_comment(value):
    if len(value) < 3:
        message = "Length of the comment must be longer"
        raise ValidationError(message)
