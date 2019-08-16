from django.urls import path
from practise_app import views

urlpatterns = [
    path('',views.users,name = 'users')
]
