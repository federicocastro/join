#! -*- encoding: utf-8 -*-
from django import template
from django.utils.translation import ugettext_lazy as _
from photologue.models import Photo

register = template.Library()


@register.filter(name='add_css_class')
def add_css_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.simple_tag(name='get_photo_url_by_slug')
def get_photo_url_by_slug(slug):
    try:
        photo = Photo.objects.get(slug=slug)
        return photo
    except Photo.DoesNotExist:
        return ''
