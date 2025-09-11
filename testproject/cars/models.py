from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Страна')  # all names will be unique

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Производитель')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна') # Linking Models

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Автомобиль')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')  # If the parent object is deleted, the related objects will be deleted too.
    start_release = models.DateField(verbose_name='Начало выпуска')
    end_release = models.DateField(null=True, blank=True, verbose_name='Окончание выпуска')  # let's make an empty line in case the release has not been discontinued

    def __str__(self):
        return self.name

class Comment(models.Model):
    email = models.EmailField(verbose_name='Email')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # actual time
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'Комментарий от {self.email} к {self.car.name}'
