from django.urls import path
from AppV import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('art/', views.articulos, name='articulo'),
    path('rub/', views.rubros, name='rubros'),
    path('cli/', views.clientes, name='clientes'),
    path('prov/', views.proveedores, name='proveedores'),
]
