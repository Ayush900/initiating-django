from django.shortcuts import render
from app1.forms import FormName
# Create your views here.

def index(request):

    return render(request,'app1/index.html')

def formpage_view(request):
    form = FormName()
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print("Validation success!")
            print("Name:"+form.cleaned_data['name'])
            print("email:"+form.cleaned_data['email_id'])
            print("text:"+form.cleaned_data['text'])

    return render(request,'app1/formpage.html',{'form':form})
