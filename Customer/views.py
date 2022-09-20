
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from .forms import UserForm,Auth_from
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth import authenticate , login 
from django.shortcuts import redirect,render
from rest_framework.renderers import TemplateHTMLRenderer
from django.views.generic import TemplateView
from .serializer import CustomerSerializer


class CreateCustomUser(generics.CreateAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'
    queryset = CustomUser.objects.all()

    def get(self, request):
        serializer = CustomerSerializer()
        form = UserForm()
        return Response({'serializer': serializer,'form':form})

    def post(self, request):
        serializer = CustomerSerializer()
        form = UserForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        return Response({'serializer': serializer,'form':form})



def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = Auth_from(request.POST)
            if forms.is_valid():
                user_model = authenticate(email=forms.cleaned_data['email'],password=forms.cleaned_data['password'])
                if user_model:
                    print(user_model)
                    login(request,user_model)
                    return HttpResponse('logged in')
            
        return render(request,"login.html")
    
    else:
        return HttpResponse('logged in')





class DashboardView(TemplateView):
    
    template_name = "index.html"

# class SignupView(CreateView):
#     form_class=UserCreationForm
#     template_name='signup.html'
#     success_url= 'login'

#     def get(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('login.html')
#         return super().get(request, *args, **kwargs)

    

# class LoginInterfaceView(LoginView):
#     template_name = 'login.html'


# class LogoutInterfaceView(LogoutView):
#     template_name= 'logout.html'

# class HomeView(TemplateView):
#     template_name = 'welcome.html'

class HomeView(TemplateView):
    template_name = 'welcome.html'

# class Apiuse(APIView):
#     def get(self, request):
#         u= CustomUser.objects.all()
#         serial = CustomerSerializer(data=u, many=True)
#         return Response(serial.data)

#     def post(self, request):
#         data = request.data
#         print(data)
#         s = CustomerSerializer(data = data)
#         if s.is_valid():
#             s.save()
#         return Response(
#             {
#                 "Saved"
#             }
#         )
    
#     def put(self, request):
#         if request.method == "PUT":
#             data = request.data
#             result = CustomUser.objects.get(id=data["id"])
#             # print(data['id'])
#         s = CustomerSerializer(result,data=data, partial=True)
#         if s.is_valid():
#             s.save()
#         return Response(
#             {
#                 "status" :"Sucess",
#                 "data": data
#             }
#         )

