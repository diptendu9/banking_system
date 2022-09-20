from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    # path('authorize', views.AuthorizedeView.as_view(), name="authorize"),
    path('register/', views.CreateCustomUser.as_view(),name="register"),

    path('login/', views.login_view, name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('api/', Apiuse.as_view()),
]