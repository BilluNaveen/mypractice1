from django.db.models import F, Q
from template import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from polls.models import *
from django.views.generic.base import View
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def view(request):
    return render(request, 'tourism.html')


def user_register(request):
    return render(request, 'registration.html')


def login_page(request):
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/")


class RegisterDetails(View):
    def post(self, request):
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        password1 = request.POST["password2"]
        if password1 == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "please already existed username")
                return redirect("/UserRegister")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"please already existed mail")
                return redirect("/UserRegister")
            else:
                User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password = password)
                return render(request, "login.html")


class UserLogin(View):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request,"please enter valid username and password")
            return redirect("/user_login")


class HomepageView(View):
    def post(self,request):
        try:
            name = request.POST["Name"]
            email = request.POST["Email"]
            phone = request.POST["Phone"]
            contactus = request.POST["ContactUs"]
            GetTouch.objects.create(name=name, email=email, phone=phone, message=contactus)
            data = {
                "success": "successfully done"
            }
            return render(request,'tourism.html',data)
        except:
            data = {
                "failure": "please enter valid data"
            }
            return render(request, 'tourism.html', data)


class Register(HomepageView):
    def get(self):
        pass


class NewsLetterView(View):
    def post(self,request):
        name=request.POST["name"]
        email=request.POST["email"]
        NewsLetter.objects.create(name=name, email=email)
        return redirect("/")