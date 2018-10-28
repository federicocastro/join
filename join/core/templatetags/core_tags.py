#! -*- encoding: utf-8 -*-
from django import template
from photologue.models import Photo
from slider.models import Slide
from core.models import ImageTitleSlug

register = template.Library()


@register.filter(name='add')
def add(value, arg):
    return str(int(value) + int(arg))


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


@register.simple_tag(name='get_image_by_slug')
def get_image_by_slug(slug):
    try:
        image = ImageTitleSlug.objects.get(slug=slug)
        return image
    except ImageTitleSlug.DoesNotExist:
        return ''


@register.simple_tag(name='get_home_sliders', takes_context=True)
def get_home_sliders(context):
    lookup = dict()
    slide_images = Slide.objects.filter(**lookup)
    return slide_images
