from django.urls import path, include
from banking.views import AccUpdate, CreateAccount, GetUserBalance, ViewAccount

urlpatterns = [
    path('create/',CreateAccount.as_view(),name = "create"),
    path('show/',ViewAccount.as_view(),name = "show"),
    path('update/<int:pk>/',AccUpdate.as_view(),name = "update"),
    path('bal/',GetUserBalance,name = "balance")
]