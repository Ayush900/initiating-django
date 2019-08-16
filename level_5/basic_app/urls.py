from django.urls import path
from basic_app import views
app_name = 'basic_app'

urlpatterns = [
    path('register/',views.registrationview,name = 'registrationview'),
    path('login/',views.user_login,name = 'login')

]
