from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Driver
from .forms import DriverForm, RegistrationForm

# Create your views here.


def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        age-=1
    return age

# ========DRIVER================

# 
# class DriverCreate(CreateView):
#     model = Driver
#     form_class = DriverModelForm
#     template_name = 'autopark/driver_form.html'

def driver_registration(request):
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        driver_form = DriverForm(request.POST)

        if reg_form.is_valid() and driver_form.is_valid():
            user = reg_form.save()
            # создали пользователя
            driver = driver_form.save(commit=False)
            driver.user = user
            driver.age = calculate_age(driver.birthday)
            driver.save()
            # return redirect('driver_profile')
            return render(request, 'autopark/driver_form.html', {'form': driver})
    
    # для метода ГЕТ
    reg_form = RegistrationForm()
    driver_form = DriverForm()
    context = {'reg_form': reg_form, 'driver_form': driver_form}
    return render(request, 'autopark/driver_form.html', context=context)


def driver_profile(request, pk):
    driver = Driver.objects.get(pk=pk)