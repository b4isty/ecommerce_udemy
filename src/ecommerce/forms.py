from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Content"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" not in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

