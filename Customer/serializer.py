from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Customer.models import CustomUser


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields ='__all__'