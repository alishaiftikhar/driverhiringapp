
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DriverProfile, ClientProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'
