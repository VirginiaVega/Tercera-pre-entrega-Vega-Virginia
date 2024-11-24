from django.db import models

# Create your models here.
class rubro(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)

class articulo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15) 
    direccion = models.CharField(max_length=255)

class proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)