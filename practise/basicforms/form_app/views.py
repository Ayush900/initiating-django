from django.shortcuts import render
from form_app.forms import FormName

# Create your views here.

def index(request):
    return render(request,'form_app/index.html')

def form_page_view(request):
    form = FormName()
    return render(request,'form_app/form_page.html',{'form':form})
