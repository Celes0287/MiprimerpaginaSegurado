from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# HOME
def home(request):
    return render(request, 'entidades/index.html')

# Usuario
def usuario(request):
    contexto = {"Usuarios": Usuario.objects.all()}
    return render(request, 'entidades/usuario.html', contexto)

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('usuario-list'))
    else:
        form = UsuarioForm() 
        
    return render(request, 'usuario_form.html', {'form': form, 'titulo': 'Crear Usuario'})

# Editar Usuario Existente
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save() 
            return redirect(reverse('usuario-list'))
    else:
        form = UsuarioForm(instance=usuario) 
        
    return render(request, 'usuario_form.html', {'form': form, 'titulo': f'Editar Usuario: {usuario.nombre}'})

# Crear Nuevo Cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('cliente-list'))
    else:
        form = ClienteForm() 
        
    return render(request, 'cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})

# Editar Cliente Existente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save() 
            return redirect(reverse('cliente-list'))
    else:
        form = ClienteForm(instance=cliente) 
        
    return render(request, 'cliente_form.html', {'form': form, 'titulo': f'Editar Cliente: {cliente.nombre}'})

# Crear Nuevo Trabajo Pedido
def crear_trabajo_pedido(request):
    if request.method == 'POST':
        form = TrabajoPedidoForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('trabajopedido-list'))
    else:
        form = TrabajoPedidoForm() 
        
    return render(request, 'trabajopedido_form.html', {'form': form, 'titulo': 'Crear Pedido'})

# Editar Trabajo Pedido Existente
def editar_trabajo_pedido(request, pk):
    trabajo = get_object_or_404(Trabajo_pedido, pk=pk)
    
    if request.method == 'POST':
        form = TrabajoPedidoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save() 
            return redirect(reverse('trabajopedido-list'))
    else:
        form = TrabajoPedidoForm(instance=trabajo) 
        
    return render(request, 'trabajopedido_form.html', {'form': form, 'titulo': f'Editar Pedido para Cliente: {trabajo.cliente.nombre}'})

# Registrar Trabajo Realizado
def crear_trabajo_realizado(request):
    if request.method == 'POST':
        form = TrabajoRealizadoForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('trabajorealizado-list'))
    else:
        form = TrabajoRealizadoForm() 
        
    return render(request, 'trabajorealizado_form.html', {'form': form})

#Editar Trabajo Realizado
def editar_trabajo_realizado(request, pk):
    trabajo = get_object_or_404(Trabajo_realizado, pk=pk)
    
    if request.method == 'POST':
        form = TrabajoRealizadoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save() 
            return redirect(reverse('trabajorealizado-list'))
    else:
        form = TrabajoRealizadoForm(instance=trabajo) 
        
    return render(request, 'trabajorealizado_form.html', {'form': form, 'titulo': f'Editar Trabajo ID: {trabajo.id}'})

#Crear Nuevo Oficio
def crear_oficio(request):
    if request.method == 'POST':
        form = OficioForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('oficio-list'))
    else:
        form = OficioForm() 
    return render(request, 'oficio_form.html', {'form': form, 'titulo': 'Crear Nuevo Oficio'})

#Editar Oficio Existente
def editar_oficio(request, pk):
    oficio = get_object_or_404(oficio, pk=pk)
    
    if request.method == 'POST':
        form = OficioForm(request.POST, instance=oficio)
        if form.is_valid():
            form.save() 
            return redirect(reverse('oficio-list'))
    else:
        form = OficioForm(instance=oficio) 
        
    return render(request, 'oficio_form.html', {'form': form, 'titulo': f'Editar Oficio: {oficio.nombre}'})

#Crear comentario para Trabajo Realizado
def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('trabajorealizado-list'))
    else:
        form = ComentarioForm() 
        
    return render(request, 'comentario_form.html', {'form': form, 'titulo': 'Agregar Comentario'})
