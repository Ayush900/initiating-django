from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email_id = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again:")
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email_id']
        vmail =all_clean_data['verify_email']

        if vmail != email:
            raise forms.ValidationError("Check that your emails match!")
