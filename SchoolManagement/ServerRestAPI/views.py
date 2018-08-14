from django.http import JsonResponse
from json import JSONEncoder

def index(request):
    """index page"""
    data ={'status': 'ok'}
    return JsonResponse(data, encoder=JSONEncoder)