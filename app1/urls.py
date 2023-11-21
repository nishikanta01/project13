from app1.views import *
from django.urls import path


app_name='nishi'
urlpatterns = [
     path('nishi/',nishi,name='nishi')
]