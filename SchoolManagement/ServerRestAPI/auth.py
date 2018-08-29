from hashlib import md5
from ServerRestAPI.models import Student, Teacher

def auth(request, mode='teacher'):
    username = request.POST.get('username')
    password = request.POST.get('password')

    password = md5(password.encode('utf-8')).hexdigest()
    user = None # user is None in default

    try:
        if mode == 'teacher':   user = Teacher.objects.get(username=username, password=password)
        elif mode == 'student': user = Student.objects.get(username=username, password=password)
    except: pass

    return user