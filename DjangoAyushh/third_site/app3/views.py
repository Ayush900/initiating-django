from django.shortcuts import render
from django.http import HttpResponse
from app3.models import Acess_record , Topic , Web_page


# Create your views here.

def index(request):
    Webpages_list = Acess_record.objects.order_by('date')
    date_dict = {'access_records':Webpages_list}
    return render(request,'app3/index.html',context=date_dict)

def arsenal(request):
    return  render(request,'app3/arsenal.html',context=None)

