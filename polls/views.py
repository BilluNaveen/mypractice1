from django.shortcuts import render
import sys
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Question


@api_view()
def home(request):
    return Response({'status':200,'message':"hello"})

def get_data(Question):
    post=Question.objects.all()
    return post

check=get_data(Question)
print(check)



# Create your views here.
