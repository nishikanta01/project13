from app2.views import *
from django.urls import path

app_name='tap'
urlpatterns=[
     path('tapan/',tapan,name='tapan')
]