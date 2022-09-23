from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .forms import UserForm
from rest_framework import generics

from django.contrib.auth import authenticate , login 
from django.shortcuts import redirect,render
# from django.views.generic import TemplateView
# from .serializer import CustomerSerializer
from django.views.generic  import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm



class SignupView(CreateView):
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

# class CreateCustomUser(generics.CreateAPIView):
    
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'register.html'
#     queryset = CustomUser.objects.all()

#     def post(self, request):
#         serializer = CustomerSerializer()
#         form = UserForm(request.POST or None)
#         # print(form)
#         if form.is_valid():
#             form.save()
#             user = CustomUser.objects.filter(email=form.changed_data['email'])

#             # if user.exists():
                
#             return redirect('login')
            
        
#         return Response({'serializer': serializer,'form':form})


# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             forms = Auth_from(request.POST)
#             if forms.is_valid():
#                 user_model = authenticate(email=forms.cleaned_data['email'],password=forms.cleaned_data['password'])
#                 if user_model:
#                     print(user_model)
#                     login(request,user_model)
                    
#                     return redirect('home')
            
#         return render(request,"login.html")
    
#     else:
#         return redirect('login')





# class DashboardView(TemplateView):
#     template_name = "index.html"

