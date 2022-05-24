
# Create your views here.
from functools import partial
import json
import re
from django.shortcuts import render
from django.http import JsonResponse
import io
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from.models import Resume
from rest_framework.parsers import JSONParser
from .serializer import ResumeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def Resume_api(request):
    if request.method == 'GET':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            get_data = Resume.objects.get(id = id)
            serializer = ResumeSerializer(get_data)
        else:
            get_data = Resume.objects.all()
            serializer = ResumeSerializer(get_data,many=True)
        print(serializer.data)
        return JsonResponse({'success':serializer.data})

    if request.method == 'POST':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        serializer = ResumeSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Data is post successfully'})
        else:
            return JsonResponse(serializer.errors)

    if request.method == 'PUT':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        obj = Resume.objects.get(id = id)
        serializer = ResumeSerializer(obj,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            obj = Resume.objects.get(id = id)
            return JsonResponse({'message':'Data is updated successfully!'})
        else:
            return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        obj = Resume.objects.get(id = python_data.get('id'))
        if python_data.get('id') is not None:
            obj.delete()
            return JsonResponse({'Message':'Data is deleted successfully! '})
        else:
            return JsonResponse({'Message':'Cannot delete!'})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def view_api(request, pk):
    res = Resume.objects.get(id = pk)
    serializer = ResumeSerializer(res)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

#all data
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def all_api(request):
    res = Resume.objects.all()
    serializer = ResumeSerializer(res, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')