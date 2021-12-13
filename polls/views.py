from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view


@api_view()
def home(request):
    return Response({'status':200,'message':"hello naveen"})

# Create your views here.
