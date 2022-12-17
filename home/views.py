from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def homepage(request):


    return HttpResponse('hello')