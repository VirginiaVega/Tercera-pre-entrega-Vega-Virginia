from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(req):
    return render(req, 'appv/index.html')

def articulo(req):
    return render(req, 'appv/articulos.html')

def rubros(req):
    return render(req, 'appv/rubros.html')

def clientes(req):
    return render(req, 'appv/clientes.html')

def proveedores(req):
    return render(req, 'appv/proveedores.html')

