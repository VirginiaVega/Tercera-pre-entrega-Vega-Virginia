from django.db import models

# Create your models here.
class Rubro(models.Model): 
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)

class Articulo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15) 
    direccion = models.CharField(max_length=255)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)