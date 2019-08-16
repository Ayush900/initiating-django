from django.urls import path
from form_app import views
urlpatterns = [
    path('',views.form_page_view,name = 'form_page_view'),
]
