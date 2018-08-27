from django.http import JsonResponse
from json import JSONEncoder
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from ServerRestAPI.models import (
    Student, Teacher, StudentLecture, 
    TeacherLecture, Lecture
    )
from ServerRestAPI.auth import teacher_auth


def index(request):
    """index page"""
    data ={'status': 'ok'}
    return JsonResponse(data, encoder=JSONEncoder)


# only teacher
@csrf_exempt
def add_grade(request):
    """add student grades"""
    teacher = teacher_auth(request)
    stu_username = request.POST.get('stu_username')
    lec_name = request.POST.get('lec_name')
    grade = request.POST.get('grade')

    if teacher != None:
        # find the student
        student = get_object_or_404(Student, username=stu_username)
        lecture = get_object_or_404(Lecture, name=lec_name)
        teacher_lecture = get_object_or_404(TeacherLecture, TeacherID=teacher, LectureID=lecture)
        stu_lectute = get_object_or_404(StudentLecture, StudentID=student, TeacherLectureID=teacher_lecture)

        stu_lectute.grade = grade
        stu_lectute.save()

    data ={'status': 'ok'}
    return JsonResponse(data, encoder=JSONEncoder)
