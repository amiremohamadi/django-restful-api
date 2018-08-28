from django.urls import re_path

from .views import index, add_grade, get_teacher_lectures

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^teacher/add-grade$', add_grade),
    re_path(r'^teacher/get-lectures$', get_teacher_lectures),
]