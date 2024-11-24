from django.contrib import admin
from .models import rubro, articulo, cliente, proveedor

# Register your models here.
admin.site.register(rubro)
admin.site.register(articulo)
admin.site.register(cliente)
admin.site.register(proveedor)