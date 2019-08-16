from django.shortcuts import render
from practise_app.models import Users

# Create your views here.

def index(request):
    return render(request,'practise_app/index.html',context=None)

def users(request):

    user_list = Users.objects.order_by('first_name')
    user_dict = { 'users' : user_list}
    return render(request,'practise_app/users.html',context=user_dict)
