from django import forms 

#FORMULARIO ORIGINAL QUE FUNCIONA:
# class RubroFormulario(forms.Form):
#     codigo = forms.CharField(max_length=10)
#     descripcion = forms.CharField(max_length=255)

class RubroFormulario(forms.Form):
    codigo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class articuloFormulario(forms.Form):
    codigo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))


class clienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))    
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class proveedorFormulario(forms.Form):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))    
    direccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))