
from email.policy import default
from telnetlib import AUTHENTICATION
from urllib import request
from rest_framework import serializers
from banking.models import Accholder, Transactions


class BankingSerializer(serializers.ModelSerializer):
   '''
   Serializer to Create Bank Account
   '''
   class Meta:
      model = Accholder
      fields = '__all__'
      
      # def create(self, validated_data):
      #    return Accholder.objects.create(**validated_data)
      def create(self, validate_data):
         user= validate_data.pop('user')
         acc = Accholder.objects.create(user=user, **validate_data)
         return acc

      def save(self, **kwargs):
         return super().save(**kwargs)



class TranasctionSerializer(serializers.ModelSerializer):
   '''
   Serializer to make Deposit and Withdraw
   '''
   class Meta:
      model = Transactions
      fields = ['user', 't_type', 'amount']



class TransferSerializer(serializers.ModelSerializer):

   '''
   Serializer to Make Transfer
   '''
   # user =  serializers.CharField(source='request.user') 
   class Meta:
      model = Transactions
      fields = ['user','t_type', 'reciver', 'amount']