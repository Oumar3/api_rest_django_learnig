from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_views(request):
    print(request.headers)
    return JsonResponse({})


