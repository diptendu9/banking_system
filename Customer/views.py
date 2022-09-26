from http.client import HTTPResponse
from urllib import request, response
from django.shortcuts import render
from rest_framework.views import APIView

from banking.models import Accholder
from .models import *
from .forms import UserForm
from rest_framework import generics

from django.contrib.auth import authenticate , login 
from django.shortcuts import redirect,render, get_object_or_404
# from django.views.generic import TemplateView
# from .serializer import CustomerSerializer
from django.views.generic  import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm



class SignupView(CreateView):
    """
    Signup view for user
    """

    form_class= UserCreationForm
    template_name='signup.html'
    success_url='/login/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    

class LoginInterfaceView(LoginView):
    template_name = 'login.html'


class LogoutInterfaceView(LogoutView):
    template_name= 'logout.html'

class HomeView(TemplateView):
    template_name = 'welcome.html'
    
    
    



