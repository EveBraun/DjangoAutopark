from django.db import models

from drivers.models import Driver
from employees.models import Car

from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    lastname = models.CharField(max_length=30, verbose_name="Фамилия")
    birthday = models.DateField(verbose_name="Дата рождения")
    age = models.IntegerField(verbose_name="Возраст")
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    email = models.EmailField(verbose_name="Эл.почта")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural="Клиенты"

    def __str__(self):
        return " ".join([self.name, self.lastname])
    

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, verbose_name='Водитель')
    
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2)
    place_from = models.CharField(max_length=100, verbose_name='Откуда')
    place_to = models.CharField(max_length=100, verbose_name='Куда')
    created_at = models.DateTimeField(default=timezone.now())
    order_date = models.DateTimeField(verbose_name='Дата и время поездки')
    comment = models.TextField(verbose_name='Комментарии', blank=True, null=True)

    def __str__(self):
        return " ".join([str(self.pk), str(self.created_at)])
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural="Заказы"
