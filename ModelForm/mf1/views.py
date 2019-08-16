from django.shortcuts import render
from mf1.forms import StudentDetailsForm
from mf1.models import StudentDetails

# Create your views here.
def index(request):
    return render(request,'mf1/index.html')

def mform_view(request):
    form = StudentDetailsForm()
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print("form validation done!")
            return index(request)
        else:
            print("form is invalid!")
    return render(request,'mf1/mform.html',{'form':form})
