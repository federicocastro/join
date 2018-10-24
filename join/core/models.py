from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from sorl.thumbnail import ImageField

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


class Image(TimeStampedModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey('authentication.User', blank=True, null=True, on_delete=models.CASCADE)
    file = ImageField(upload_to='images')


class Comment(TimeStampedModel):
    comment = models.TextField()
    author = models.ForeignKey('authentication.User',
                               blank=True, null=True, related_name='comments',
                               on_delete=models.PROTECT)
