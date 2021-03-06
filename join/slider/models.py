from django.db import models
from sorl.thumbnail import ImageField
from django_extensions.db.models import (
    TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel,)


class Slide(TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel):
    image = ImageField(upload_to='slides')
    show_btn = models.BooleanField(default=False)
    btn_text = models.CharField(max_length=40, blank=True, null=True)
    btn_link = models.URLField(blank=True, null=True)
    btn_view_name = models.CharField(max_length=100, blank=True, null=True)
    is_public = models.BooleanField(default=True)

    resize_to = models.CharField(default="1920x1080", max_length=30)
    quality = models.CharField(default="15", max_length=30)
    format = models.CharField(default="PNG", max_length=30)
