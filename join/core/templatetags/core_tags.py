#! -*- encoding: utf-8 -*-
from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.filter(name='add_css_class')
def add_css_class(value, arg):
    return value.as_widget(attrs={'class': arg})
