from django.db import models
from Customer.models import *
import random
from django.contrib.auth.models import User

class Accholder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    account_number = models.IntegerField(default=random.randint(00000000,999999999),unique=True)
    atypes = (
        ('S', 'Savings'),
        ('C', 'Current')
    )
    acc_type = models.CharField(max_length=1, choices=atypes)
    balance = models.PositiveIntegerField(default=0)
    pan= models.CharField(max_length=100)
    aadhaar = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    
class Transactions(models.Model):
    user = models.ForeignKey(Accholder,related_name = "sender",on_delete=models.CASCADE)
    reciver = models.ForeignKey(Accholder,related_name = "receiver",on_delete=models.CASCADE)
    amount = models.FloatField()
    transfer_date= models.DateTimeField(auto_now=True)
    transact_date= models.DateTimeField(auto_now=True) 

