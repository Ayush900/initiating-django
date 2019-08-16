from django.shortcuts import render
from form_app.forms import Football_Form

# Create your views here.

def home(request):
    return render(request,'form_app/home.html')

def football_Form_view(request):
    form = Football_Form()
    if request.method == "POST":
        form = Football_Form(request.POST)
        if form.is_valid():
            print("Validation Success!!")
            print("Name of the supporter:"+form.cleaned_data['name'])
            print("Favourite team is:"+form.cleaned_data['fav_team'])
            print("It's slogans for the fans are:\n"+form.cleaned_data['slogan'])
    return render(request,'form_app/form_page.html',{'form':form})
