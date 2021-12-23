
# Create your models here.

from django.db import models

class GetTouch(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=254, null=True)
    phone = models.BigIntegerField(null=True)
    message = models.TextField(null=True, default="")

class NewsLetter(models.Model):
    name=models.CharField(max_length=100, null=True, unique=True)
    email=models.EmailField(max_length=254, null=True, unique=True)