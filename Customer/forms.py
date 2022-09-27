import email
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

class UserForm(forms.Form):
    
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    email = forms.EmailField(help_text = "Enter your email id")
    password = forms.CharField(widget = forms.PasswordInput())
    