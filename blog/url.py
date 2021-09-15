from user.views import *
from django.contrib import admin
from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path("sign",sign,name="sign"),
    path('signup',SignUp.as_view(),name="signup"),
    path('profil',profil,name="profil"),
    path('change_password',Change_password.as_view(),name="change_password"),
    path("logout",logout_view,name="logout")
]
