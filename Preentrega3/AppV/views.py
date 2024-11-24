from django.shortcuts import render
from .models import rubro, articulo, cliente, proveedor
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
            rubro_obj = rubro(codigo=informacion["codigo"], descripcion=informacion["descripcion"])
            rubro_obj.save()
            return render(req, "appv/index.html")  # Redirigir o mostrar algún mensaje
    else:
        miFormulario = RubroFormulario()
    return render(req, 'appv/rubros.html', {"miFormulario": miFormulario})


def articulos(req):
    if req.method == 'POST':
        miFormulario = articuloFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = articulo(codigo=informacion["codigo"], descripcion=informacion["descripcion"], precio=informacion["precio"]) #, rubro=informacion["rubro"] lo elimine por ahora
            rubro_obj.save()
            return render(req, "appv/index.html")  # Redirigir o mostrar algún mensaje
    else:
        miFormulario = articuloFormulario()
    return render(req, 'appv/articulos.html', {"miFormulario": miFormulario})



def clientes(req):
    if req.method == 'POST':
        miFormulario = clienteFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = cliente(nombre=informacion["nombre"], email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"]) 
            rubro_obj.save()
            return render(req, "appv/index.html")  # Redirigir o mostrar algún mensaje
    else:
        miFormulario = clienteFormulario()
    return render(req, 'appv/clientes.html', {"miFormulario": miFormulario})



def proveedores(req):
    if req.method == 'POST':
        miFormulario = proveedorFormulario(req.POST)
        print(miFormulario) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            rubro_obj = proveedor(nombre=informacion["nombre"], email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"]) 
            rubro_obj.save()
            return render(req, "appv/index.html")  # Redirigir o mostrar algún mensaje
    else:
        miFormulario = proveedorFormulario()
    return render(req, 'appv/proveedores.html', {"miFormulario": miFormulario})


