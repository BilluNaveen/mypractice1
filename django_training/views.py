from django.db.models import F,Q
from template import *
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import *



def view(request):

    # e=Address.objects.values(customer_name=F('customer__name'))
    # print(e)
    return render(request,'tourism.html')

def homePageView(request):
    if request.method=="POST":
        try:
            name=request.POST["Name"]
            email=request.POST["Email"]
            phone=request.POST["Phone"]
            contactus=request.POST["ContactUs"]
            Customer.objects.create(name=name,email=email,phone=phone,message=contactus)
            data={
                "success":"successfully done"
            }
            return render(request, 'tourism.html',data)
        except:
            data = {
                "failure":"please enter valid data"
            }
            return render(request,'tourism.html',data)
            # except:
            #
            #     return rednder(request,'tourism.html',data)