from django import template
from django.shortcuts import get_object_or_404
from ..models import Setting

register = template.Library()

@register.simple_tag
def MSCE_set():
    return get_object_or_404(Setting, id=1)