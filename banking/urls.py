from django.urls import path, include
from banking.views import CreateAccount, ViewAccount

urlpatterns = [
    path('create/',CreateAccount.as_view(),name = "create"),
    path('show/',ViewAccount.as_view(),name = "show")
]