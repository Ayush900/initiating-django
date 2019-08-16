from django.urls import path
from app3 import  views

urlpatterns = [
    path('',views.arsenal,name = 'arsenal'),
]