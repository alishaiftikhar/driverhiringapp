
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import DriverProfile, ClientProfile
from .serializers import UserSerializer, DriverSerializer, ClientSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = DriverProfile.objects.all()
    serializer_class = DriverSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientSerializer

    
