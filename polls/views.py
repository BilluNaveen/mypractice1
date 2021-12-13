from django.shortcuts import render
import sys
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Question

from .serializer import questionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
#
# @api_view(["POST"])
# def home(request):
#     return Response({'status':200,'message':"hello"})

class QuestionList(APIView):

    def get(self,request):
        post=Question.objects.all()
        serializer=questionSerializer(post,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass


# Create your views here.
