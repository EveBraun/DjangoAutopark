
from django.urls import path

from .views import driver_registration, driver_profile

urlpatterns = [
    path('create/', driver_registration, name='driver_registration'),
    path('profile/', driver_profile, name='driver_profile')
]
