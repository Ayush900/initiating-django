from django import forms
from basic_app.models import TeamProfile

class TeamProfileForm(forms.ModelForm):
    password = forms.CharField(max_length=None,widget = forms.PasswordInput)
    class Meta:
        model = TeamProfile
        fields = "__all__"
