from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DriverViewSet, ClientViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('drivers', DriverViewSet)
router.register('clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
