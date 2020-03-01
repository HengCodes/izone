from django.urls import path
from .views import (TopicView,TopicListView)

urlpatterns = [
    path('courses/', TopicView, name='courses'),  # 教程汇总页
    path('course_list/', TopicListView, name='course_list'),  # 教程目录页
    # path('courses/<slug:slug>/', CourseView.as_view(), name='courses'),
]