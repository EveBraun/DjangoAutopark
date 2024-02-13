from .views import register, register_done, index, log_in
from django.urls import path

app_name = 'drivers'
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name="register"),
    path('register-done/', register_done, name="register_done"),
    path('login/', log_in, name="login"),
    # path('profile/', profile, name="profile"),
    
]