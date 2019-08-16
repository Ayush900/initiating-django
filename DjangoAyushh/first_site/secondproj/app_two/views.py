from django.shortcuts import render

# Create your views here.

def help(request):
    my_dict = {'help':"HELP PAGE!!"}
    return render(request,'app_two/help.html',context=my_dict)