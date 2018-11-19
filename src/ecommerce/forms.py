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


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        mail = User.objects.filter(email=email)
        if mail.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean_password(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Password must match.")
        return data
