from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


#get data on pgadmin4

from polls.models import *
from polls.serializer import *

@api_view()
def HelloView(request):
    obj = Question.objects.all()
    serializer=questionSerializer(obj,many=True)
    return Response(serializer.data)



#
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)             # <-- And here
#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)