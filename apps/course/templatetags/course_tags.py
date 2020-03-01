# -*- coding: utf-8 -*-
from django import template

from ..models import CourseTopic

register = template.Library()


@register.simple_tag
def get_topics():
    '''获取教程分类'''
    return CourseTopic.objects.all()
#
# @register.simple_tag
# def get_toollinks(cate):
#     '''获取单个教程下所有课程'''
#     return cate.toollink_set.all()
