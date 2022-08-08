from django.db import models

# Create your models here.
class Blusas(models.Model):
    nombre = models.CharField(max_length=150)
    talla = models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.FileField()
    stock= models.IntegerField()

class Pantalones(models.Model):
    nombre= models.CharField(max_length=150)
    talla = models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.FileField()
    stock= models.IntegerField()

class Busos(models.Model):
    nombre= models.CharField(max_length=150)
    talla= models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.FileField()
    stock= models.IntegerField()

class Medias(models.Model):
    nombre= models.CharField
    talla= models.CharField
    precio= models.FloatField
    imagen= models.FileField
    stock= models.IntegerField

def __str__(self):
    return f"{self.name}, {self.talla}, {self.precio}, {self.imagen}, {self.stock}"

