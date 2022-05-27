from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("this email is already existed.")
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("this username is already existed.")
        return username


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords is not match")

class UserLoginForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
     password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'form-control'}))


