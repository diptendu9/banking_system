from django.db import models
from Customer.models import *
from django.conf import settings
import random
from bankproject.settings import AUTH_USER_MODEL 
# Create your models here.

class Accholder(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.IntegerField(default=random.randint(00000000,999999999),unique=True)
    atypes = (
        ('S', 'Savings'),
        ('C', 'Current')
    )
    acc_type = models.CharField(max_length=1, choices=atypes)
    balance = models.PositiveIntegerField(default=0)
    pan= models.CharField(max_length=100)
    aadhaar = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name