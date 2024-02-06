from django.db import models
from .enums import car_categories, car_colors

class Driver(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(editable=False, verbose_name='Возраст')
    passport = models.CharField(max_length=11, verbose_name='Паспорт')
    is_available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return ' '.join([self.name, self.lastname])
    
    def get_age():
        pass


class CarBrand(models.Model):   
    name = models.CharField(max_length=20, verbose_name='Бренд')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'  


class Car(models.Model):
    
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Бренд')
    model = models.CharField(max_length=20, verbose_name='Модель')
    color = models.CharField(max_length=20, choices=car_colors, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name='Изображение')
    category = models.CharField(max_length=20, choices=car_categories, verbose_name='Класс')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return ' '.join([self.brand__name, self.model, self.year])



class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    lastname = models.CharField(max_length=20, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Эл. почта')
    age = models.IntegerField(verbose_name='Возраст')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        def __str__(self):
            return ' '.join([self.name, self.lastname])
