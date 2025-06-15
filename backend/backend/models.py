from django.db import models
from django.contrib.auth.models import User

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)
    age = models.IntegerField()
    license_number = models.CharField(max_length=50)
    license_expiry = models.DateField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

