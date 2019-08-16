from mf1.models import StudentDetails
from django import forms

class StudentDetailsForm(forms.ModelForm):




    class Meta:
        model = StudentDetails
        fields = '__all__'
