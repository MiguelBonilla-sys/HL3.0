from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def to_image(value):
    return mark_safe(f'data:image/png;base64,{value}')
