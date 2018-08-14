from django.contrib import admin
from ServerRestAPI.models import (Student, Teacher, StudentLecture)


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentLecture)