from django import forms

class Football_Form(forms.Form):
    name = forms.CharField()
    fav_team = forms.CharField()
    slogan = forms.CharField(widget = forms.Textarea)
    
