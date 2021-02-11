from django.core.exceptions import Validation error


def file_size(value):
    filesize=value.size
    if filesize > 10000000:
        raise ValidationError("maximum size is 10 mb")
