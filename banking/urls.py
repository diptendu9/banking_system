from django.urls import path, include
from banking.views import CreateAccount

urlpatterns = [
    path('create/',CreateAccount.as_view(),name = "create")

]