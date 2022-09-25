
from email.policy import default
from telnetlib import AUTHENTICATION
from urllib import request
from rest_framework import serializers
from banking.models import Accholder, Transactions, Transfers


class BankingSerializer(serializers.ModelSerializer):
   
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

   class Meta:
      model = Transactions
      fields = '__all__'



class TransferSerializer(serializers.ModelSerializer):
   # user =  serializers.CharField(source='request.user') 
   class Meta:
      model = Transfers
      fields = '__all__'