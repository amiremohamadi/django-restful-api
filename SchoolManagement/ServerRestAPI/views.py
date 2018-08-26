from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt

from ServerRestAPI.models import Student, Teacher
from ServerRestAPI.auth import teacher_auth

def index(request):
    """index page"""
    data ={'status': 'ok'}
    return JsonResponse(data, encoder=JSONEncoder)

# only teacher
@csrf_exempt
def add_grade(request):
    """add student grades"""
    auth = teacher_auth(request)
    print(auth)
    a = Student.objects.filter(name="amir").prefetch_related(
        'le', 'playerstats_set')
    print(a)
    data ={'status': 'ok'}
    return JsonResponse(data, encoder=JSONEncoder)
