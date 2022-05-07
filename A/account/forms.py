from django import forms

class UserRegisterationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()