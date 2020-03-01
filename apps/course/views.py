from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.conf import settings
from .models import CourseClauses,CourseTopic

# Create your views here.

def TopicView(request):
    return render(request, 'course/base_tool.html')


def TopicListView(request):
    return render(request, 'course/course_list.html')

