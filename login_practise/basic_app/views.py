from django.shortcuts import render
from basic_app.forms import TeamProfileForm
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

registered_teams = []

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def registered_teams_view(request):
    return render(request,'registered_teams.html',{'registered_teams':registered_team})



def registrationview(request):
    registered = False
    team_profile_form = TeamProfileForm()
    if request.method == 'POST':
        team_profile_form = TeamProfileForm(data = request.POST)
        if team_profile_form.is_valid():
            TN = request.POST.get('username')
            registered_teams.append(TN)
            team_profile_form.save()
            registered = True

        else:
            print(team_profile_form.errors)
    else:
        team_profile_form = TeamProfileForm()

    return render(request,'basic_app/registration.html',{'team_profile_form':team_profile_form,
                                                         'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active!")
        else:
            return HttpResponse("This team is not registered!\nPlease check the details again!")

    else:
        return render(request,'basic_app/login.html',{})
