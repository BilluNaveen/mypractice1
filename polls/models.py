
# Create your models here.

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length = 254,null = True)
    phone=models.CharField(max_length=100,null = True)
    message=models.TextField(null=True)
