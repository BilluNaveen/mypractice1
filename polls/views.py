from django.shortcuts import render
import sys
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Question

from .serializer import questionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view()
def get_data(request):
    obj=Question.objects.all()
    serializer=questionSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def post_data(request):
    serializer=questionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def update_data(request):
    obj = Question.objects.get(id=id)
    serializer=questionSerializer(instance=obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_data(request,id):
    obj = Question.objects.get(id=id)
    obj.delete()
    # serializer=questionSerializer(data=request.data)
    return Response("done")
