from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from banking.models import Accholder


class BankingSerializer(serializers.ModelSerializer):
     class Meta:
        model = Accholder
        fields = '__all__'