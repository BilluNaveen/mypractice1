
# Create your models here.

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length = 254,null=True)
    phone=models.BigIntegerField(null=True)
    message=models.TextField(null=True,default="")


class Address(models.Model):
    customer=models.ForeignKey(Customer, related_name="address", on_delete=models.CASCADE,null=True)
    pin=models.BigIntegerField(null=True)
