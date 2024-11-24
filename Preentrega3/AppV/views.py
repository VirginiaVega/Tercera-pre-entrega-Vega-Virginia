from django.shortcuts import render
from .models import Rubro, Articulo, Cliente, Proveedor
from AppV.forms import RubroFormulario, articuloFormulario, clienteFormulario, proveedorFormulario

# Create your views here.
def inicio(req):
    return render(req, 'appv/index.html')


def rubros(req):
    if req.method == 'POST':
        miFormulario = RubroFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = Rubro(codigo=informacion["codigo"], descripcion=informacion["descripcion"])
            rubro_obj.save()
            return render(req, "appv/index.html")
    else:
        miFormulario = RubroFormulario()
    return render(req, 'appv/rubros.html', {"miFormulario": miFormulario})


def articulos(req):
    if req.method == 'POST':
        miFormulario = articuloFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = Articulo(codigo=informacion["codigo"], descripcion=informacion["descripcion"], precio=informacion["precio"]) #, rubro=informacion["rubro"] lo elimine por ahora
            rubro_obj.save()
            return render(req, "appv/index.html")
    else:
        miFormulario = articuloFormulario()
    return render(req, 'appv/articulos.html', {"miFormulario": miFormulario})



def clientes(req):
    if req.method == 'POST':
        miFormulario = clienteFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = Cliente(nombre=informacion["nombre"], email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"]) 
            rubro_obj.save()
            return render(req, "appv/index.html")
    else:
        miFormulario = clienteFormulario()
    return render(req, 'appv/clientes.html', {"miFormulario": miFormulario})



def proveedores(req):
    if req.method == 'POST':
        miFormulario = proveedorFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = Proveedor(nombre=informacion["nombre"], email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"]) 
            rubro_obj.save()
            return render(req, "appv/index.html") 
    else:
        miFormulario = proveedorFormulario()
    return render(req, 'appv/proveedores.html', {"miFormulario": miFormulario})





def buscarArticulo(req):
    articulos= []
    codigo= req.GET.get("codigo")
    if codigo:
        articulos = Articulo.objects.filter(codigo__icontains=codigo)
    return render(req, "appv/index.html", {"codigo":codigo, "articulos":articulos})


