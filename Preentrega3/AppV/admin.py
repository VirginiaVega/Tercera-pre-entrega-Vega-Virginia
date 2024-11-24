from django.contrib import admin
from .models import Rubro, Articulo, Cliente, Proveedor

# Register your models here.
admin.site.register(Rubro)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Proveedor)