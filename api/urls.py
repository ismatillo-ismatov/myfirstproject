
from django.urls import path
from api.views  import *



app_name = 'api'

urlpatterns = [
    path("categorys/",categorys_api,name="categorys_api")    
]
