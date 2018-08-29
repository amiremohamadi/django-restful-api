from django.urls import re_path

from .views import (
    index, add_grade, get_teacher_lectures, 
    get_student_lectures
    )

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^teacher/add-grade$', add_grade),
    re_path(r'^teacher/get-lectures$', get_teacher_lectures),
    re_path(r'^student/get-lectures$', get_student_lectures),
]