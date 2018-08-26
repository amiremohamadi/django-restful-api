from django.urls import re_path

from .views import index, add_grade

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^teacher/add_grade$', add_grade),
]