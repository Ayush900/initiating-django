from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('login/',views.user_login,name = 'login'),
    path('registration/',views.registrationview,name = 'registration'),


]
