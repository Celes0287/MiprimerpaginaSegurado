from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
<<<<<<< HEAD
        fields = ['nombre', 'apellido', 'telefono', 'email', 'oficios', 'matricula']
=======
        fields = ['nombre', 'apellido', 'telefono', 'email', 'contraseña', 'oficios', 'matricula']
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email']

class TrabajoPedidoForm(forms.ModelForm):
    class Meta:
        model = Trabajo_pedido
        fields = ['cliente', 'descripcion', 'fecha_acordada']

class TrabajoRealizadoForm(forms.ModelForm):
    class Meta:
        model = Trabajo_realizado
        fields = ['trabajo_pedido', 'descripcion', 'realizado']

class OficioForm(forms.ModelForm):
    class Meta:
        model = Oficio
        fields = ['nombre', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['trabajo_realizado', 'usuario', 'texto']
