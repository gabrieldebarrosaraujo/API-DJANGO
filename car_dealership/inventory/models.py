from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

class Car(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=50)

class Feature(models.Model):
    name = models.CharField(max_length=255)
    cars = models.ManyToManyField(Car, related_name='features')
