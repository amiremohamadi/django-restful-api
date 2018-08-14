from django.contrib import admin
from ServerRestAPI.models import (
    Student, Teacher, StudentLecture, 
    TeacherLecture, Lecture
    )


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentLecture)
admin.site.register(TeacherLecture)
admin.site.register(Lecture)