from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Blusas(models.Model):
    nombre= models.CharField(max_length=150)
    talla= models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)
    stock= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} -Talla: {self.talla} - Precio: {self.precio} - Imagen: {self.imagen}  Stock:{self.stock}"
class Pantalones(models.Model):
    nombre= models.CharField(max_length=150)
    talla = models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)
    stock= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} -Talla: {self.talla} - Precio: {self.precio} - Imagen:  {self.imagen}  Stock: {self.stock}"

class Busos(models.Model):
    nombre= models.CharField(max_length=150)
    talla= models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)
    stock= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} -Talla: {self.talla} - Precio: {self.precio} - Imagen: {self.imagen}  Stock: {self.stock}"

class Medias(models.Model):
    nombre= models.CharField(max_length=150)
    talla= models.CharField(max_length=150)
    precio= models.FloatField()
    imagen= models.ImageField(upload_to="avatares", null=True, blank=True)
    stock= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} -Talla{self.talla} - Precio {self.precio} - Imagen {self.imagen}  Stock-{self.stock}"
  
class Avatar(models.Model):
    user= models.ForeignKey (User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

    def get_image_filename(instance, filename):
        title= "titulo"
        slug= slugify(title)
        return "imagenesAvatares/%s-%s" % (slug, filename)

