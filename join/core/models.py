from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django_extensions.db.models import (
    TimeStampedModel, TitleDescriptionModel, ActivatorModel, TitleSlugDescriptionModel,)


class File(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    name = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='content')
    type = models.CharField(max_length=50, blank=True, null=True)

    uploaded_by = models.ForeignKey('authentication.User', blank=True, null=True,
                                    related_name='files', on_delete=models.CASCADE)
