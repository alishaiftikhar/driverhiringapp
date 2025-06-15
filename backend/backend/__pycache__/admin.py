from django.contrib import admin
from .models import DriverProfile, ClientProfile

admin.site.register(DriverProfile)
admin.site.register(ClientProfile)

@admin.register(DriverProfile)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'license_number', 'license_expiry','cnic','adress')

@admin.register(ClientProfile)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'cnic','age',)
