from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_views(request):
    data = {
        'nom':'Oumar',
        'prenom':'Ali',
        'age':26
    }

    return JsonResponse(data)
