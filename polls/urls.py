
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", view),
    path("UserRegister",user_register),
    path("user_login", login_page),
    path("logout",logout_page),
    path("login_details",UserLogin.as_view()),
    path("register_details",RegisterDetails.as_view()),
    path("register",HomepageView.as_view()),
    path("newsletter",NewsLetterView.as_view())
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)