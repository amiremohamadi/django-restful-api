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
        try:    student = Student.objects.get(username=stu_username)
        except: return JsonResponse(
            {'message' : 'student not found!'}, 
            encoder=JSONEncoder, 
            status=404)
        # find the lecture
        try:    lecture = Lecture.objects.get(name=lec_name)
        except: return JsonResponse(
            {'message' : 'lecture not found!'}, 
            encoder=JSONEncoder, 
            status=404)
        # find if teacher has this lecture
        try:    teacher_lecture = TeacherLecture.objects.get(
            TeacherID=teacher, 
            LectureID=lecture)
        except: return JsonResponse(
            {'message' : 'teacher has no lecture called %s' %(lec_name)}, 
            encoder=JSONEncoder, 
            status=404)
        # find if student has this lecture        
        try:    stu_lecture = StudentLecture.objects.get(
            StudentID=student, 
            TeacherLectureID=teacher_lecture)
        except: return JsonResponse(
            {'message' : 'student has no lecture called %s' %(lec_name)}, 
            encoder=JSONEncoder)

        # data validation
        if int(grade) > 20:     grade = '20'
        elif int(grade) < 0:    grade = '0'
        # do changes and save
        stu_lecture.grade = grade
        stu_lecture.save()
    
    else:   return JsonResponse(
        {'message' : 'can\'t login!'}, 
        encoder=JSONEncoder, status=401)

    return JsonResponse(
        {'message': 'successful'}, 
        encoder=JSONEncoder, status=200)


@csrf_exempt
def get_teacher_lectures(request):
    teacher = teacher_auth(request)
    data = []

    if teacher != None:
        lectures = teacher.teacherlecture_set.all()
        data = [str(lecture.LectureID) for lecture in lectures]
    
    else:   return JsonResponse(
        {'message' : 'can\'t login!'},
         encoder=JSONEncoder, safe=False, status=401)


    return JsonResponse(
        data, encoder=JSONEncoder, safe=False, status=200)
