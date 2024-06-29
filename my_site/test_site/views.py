from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, views
from django.http import JsonResponse
import json
import tensorflow as tf
import numpy as np
from .AI import *

class index(views.APIView):
    def __init__(self, *args, **kwargs):
        super(index, self).__init__(*args, **kwargs)
      
    def get(self,request:HttpRequest)-> HttpResponseRedirect:
        return render(request,'temp1/AI.html')

@csrf_exempt
def my_view(request):
    global model
    print(request.method)
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        response_data = {'predictions': predict_with_model(data)}
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)