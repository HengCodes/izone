# -*- coding: utf-8 -*-
from django import template

from ..models import Course

register = template.Library()


@register.simple_tag
def get_topics():
    '''获取教程分类'''
    return Course.objects.all()
