
from template import *
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Customer



def view(request):
    Customer.objects.filter(name="mahesh",phone=1234).update(name="ramesh")
    return render(request,'tourism.html')

def homePageView(request):
    if request.method=="POST":
        name=request.POST["Name"]
        email=request.POST["Email"]
        phone=request.POST["Phone"]
        contactus=request.POST["ContactUs"]
        Customer.objects.create(name=name,email=email,phone=phone,message=contactus)
        data={
            "success":"successfully done"
        }
        return render(request, 'tourism.html',data)

    else:
        return HttpResponse("Hello, World!")