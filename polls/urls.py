
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_data),
    path('post/', post_data),
    path('update/<int:id>/', update_data),
    path('delete/<int:id>/', delete_data),
]