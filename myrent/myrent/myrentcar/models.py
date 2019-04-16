from django.db import models
from .choices import SEGMENT_CHOICES

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    segment = models.CharField(max_length=2, choices=SEGMENT_CHOICES, default='A')
    rents = models.ManyToManyField('Client', through='Rent')

    def __repr__(self):
        return f'brand: {self.brand}, model: {self.model}, segment: {self.segment}'


class Client(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __repr__(self):
        return f'name: {self.name}, last name: {self.last_name} '


class Rent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    data_start = models.DateField()
    date_end = models.DateField()









