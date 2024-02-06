from django.shortcuts import render
from django.views.generic import CreateView

from .models import Driver
from .forms import DriverModelForm

# Create your views here.

# ========DRIVER================

class DriverCreate(CreateView):
    model = Driver
    form_class = DriverModelForm
    template_name = 'autopark/driver_form.html'
