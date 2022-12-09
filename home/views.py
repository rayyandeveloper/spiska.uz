from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import *


def homepage(request):
    response = []

    for i in Region.objects.all():
        t = {'name': i.name, 'districts' : [{'name' : j.name} for j in District.objects.filter(region=i)]}
        
        response.append(t)

    return Response(response)
