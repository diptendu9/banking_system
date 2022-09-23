
from email.policy import default
from telnetlib import AUTHENTICATION
from urllib import request
from rest_framework import serializers
from banking.models import Accholder, Transactions


class BankingSerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Accholder
      fields = ['user','name','email','acc_type','pan', 'aadhaar']
      # def create(self, validated_data):
      #    return Accholder.objects.create(**validated_data)


class TranasctionSerializer(serializers.ModelSerializer):

   class Meta:
      model = Transactions
      fields = ['user', 'reciver', 'amount', 'transfer_date', 'transact_date']