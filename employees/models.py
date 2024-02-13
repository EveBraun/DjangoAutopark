from django.db import models
from .enums import car_categories, car_colors

class CarBrand(models.Model):
    name = models.CharField(max_length=20, verbose_name="Бренд")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Car(models.Model):   
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="cars", verbose_name="Бренд")
    model = models.CharField(max_length=20, verbose_name="Модель")
    color = models.CharField(max_length=20, choices=car_colors, verbose_name="Цвет")
    power = models.IntegerField(verbose_name="Мощность")
    year = models.IntegerField(verbose_name="Год выпуска")
    image = models.ImageField(upload_to="cars/", blank=True, null=True, verbose_name="Изображение")
    category = models.CharField(max_length=10, choices=car_categories, verbose_name="Класс")

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural="Машины"

    def __str__(self):
        return " ".join([self.brand, self.model, self.year])

