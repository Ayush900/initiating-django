from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi! Ayush Mehrotra here!!")


def help(request):
    my_dict = {'help_insert' : "Help Page!!"}
    return render(request,'second_app/help.html',context=my_dict)
