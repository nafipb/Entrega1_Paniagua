from django.urls import path
from SoCasual.views import *

urlpatterns = [
    path("",index, name= "inicio")
]