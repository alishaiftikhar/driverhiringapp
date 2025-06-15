from django.urls import path, include
from rest_framework import routers
from .views import DriverProfileViewSet, ClientProfileViewSet

router = routers.DefaultRouter()
router.register(r'drivers', DriverProfileViewSet)
router.register(r'clients', ClientProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
