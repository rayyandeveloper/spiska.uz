from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import *

@api_view(["GET", "POST"])
def homepage(request):
    response = []

    if request.method == "POST":
        data = request.data.get('data')
        
        for i in data:
            obj = Region.objects.create(name=i['name'])
            for x in i['districts']:
                District.objects.create(name=x['name'], region=obj)

        return Response({'status': 200})


            
    


    for i in Region.objects.all():
        t = {'name': i.name, 'districts' : [{'name' : j.name} for j in District.objects.filter(region=i)]}
        
        response.append(t)

    return Response(response)
