from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

@register.simple_tag
def settings_dict(name,key):
    return getattr(settings, name, "")[key]

