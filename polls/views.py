from django.shortcuts import render
import sys
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Question

from .serializer import questionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

@api_view(["GET"])

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_data(request):
    obj=Question.objects.all()
    serializer=questionSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post_data(request):
    serializer=questionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_data(request):
    obj = Question.objects.get(id=id)
    serializer=questionSerializer(instance=obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_data(request,id):
    obj = Question.objects.get(id=id)
    obj.delete()
    # serializer=questionSerializer(data=request.data)
    return Response("done")
