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
<<<<<<< HEAD
    return render(request, 'entidades/usuario_list.html', contexto)
=======
    return render(request, 'entidades/usuario.html', contexto)
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:usuario-list'))
    else:
        form = UsuarioForm() 
            
    return render(request, 'entidades/usuario_form.html', {'form': form, 'titulo': 'Crear Usuario'})
=======
            return redirect(reverse('usuario-list'))
    else:
        form = UsuarioForm() 
        
    return render(request, 'usuario_form.html', {'form': form, 'titulo': 'Crear Usuario'})
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

# Editar Usuario Existente
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:usuario-list'))
    else:
        form = UsuarioForm(instance=usuario) 
        
    return render(request, 'entidades/usuario_form.html', {'form': form, 'titulo': f'Editar Usuario: {usuario.nombre}'})

# Cliente
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'entidades/cliente_list.html', {'clientes': clientes})


=======
            return redirect(reverse('usuario-list'))
    else:
        form = UsuarioForm(instance=usuario) 
        
    return render(request, 'usuario_form.html', {'form': form, 'titulo': f'Editar Usuario: {usuario.nombre}'})

# Crear Nuevo Cliente
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST) 
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:cliente-list'))
    else:
        form = ClienteForm() 
        
    return render(request, 'entidades/cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})
=======
            return redirect(reverse('cliente-list'))
    else:
        form = ClienteForm() 
        
    return render(request, 'cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

# Editar Cliente Existente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:cliente-list'))
    else:
        form = ClienteForm(instance=cliente) 
        
    return render(request, 'entidades/cliente_form.html', {'form': form, 'titulo': f'Editar Cliente: {cliente.nombre}'})

# Trabajo Pedido
def listar_trabajo_pedido(request):
    trabajos_pedidos = Trabajo_pedido.objects.all()
    return render(request, 'entidades/trabajo_pedido_list.html', {'trabajo_pedido': trabajos_pedidos})

=======
            return redirect(reverse('cliente-list'))
    else:
        form = ClienteForm(instance=cliente) 
        
    return render(request, 'cliente_form.html', {'form': form, 'titulo': f'Editar Cliente: {cliente.nombre}'})

# Crear Nuevo Trabajo Pedido
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
def crear_trabajo_pedido(request):
    if request.method == 'POST':
        form = TrabajoPedidoForm(request.POST) 
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:trabajo-pedido-list'))
    else:
        form = TrabajoPedidoForm() 
        
    return render(request, 'entidades/trabajo_pedido_form.html', {'form': form, 'titulo': 'Crear Pedido'})
=======
            return redirect(reverse('trabajopedido-list'))
    else:
        form = TrabajoPedidoForm() 
        
    return render(request, 'trabajopedido_form.html', {'form': form, 'titulo': 'Crear Pedido'})
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

# Editar Trabajo Pedido Existente
def editar_trabajo_pedido(request, pk):
    trabajo = get_object_or_404(Trabajo_pedido, pk=pk)
    
    if request.method == 'POST':
        form = TrabajoPedidoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:trabajo-pedido-list'))
    else:
        form = TrabajoPedidoForm(instance=trabajo) 
        
    return render(request, 'entidades/trabajo_pedido_form.html', {'form': form, 'titulo': f'Editar Pedido para Cliente: {trabajo.cliente.nombre}'})

# Trabajo Realizado
def listar_trabajos_realizados(request):
    trabajos_realizados = Trabajo_realizado.objects.all()
    return render(request, 'entidades/trabajo_realizado_list.html', {'trabajos_realizados': trabajos_realizados})

=======
            return redirect(reverse('trabajopedido-list'))
    else:
        form = TrabajoPedidoForm(instance=trabajo) 
        
    return render(request, 'trabajopedido_form.html', {'form': form, 'titulo': f'Editar Pedido para Cliente: {trabajo.cliente.nombre}'})

# Registrar Trabajo Realizado
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
def crear_trabajo_realizado(request):
    if request.method == 'POST':
        form = TrabajoRealizadoForm(request.POST) 
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:trabajo-realizado-list'))
    else:
        form = TrabajoRealizadoForm() 
        
    return render(request, 'entidades/trabajo_realizado_form.html', {'form': form})
=======
            return redirect(reverse('trabajorealizado-list'))
    else:
        form = TrabajoRealizadoForm() 
        
    return render(request, 'trabajorealizado_form.html', {'form': form})
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

#Editar Trabajo Realizado
def editar_trabajo_realizado(request, pk):
    trabajo = get_object_or_404(Trabajo_realizado, pk=pk)
    
    if request.method == 'POST':
        form = TrabajoRealizadoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:trabajo-realizado-list'))
    else:
        form = TrabajoRealizadoForm(instance=trabajo) 
        
    return render(request, 'entidades/trabajo_realizado_form.html', {'form': form, 'titulo': f'Editar Trabajo ID: {trabajo.id}'})

#Oficio

def listar_oficios(request):
    oficios = Oficio.objects.all()
    return render(request, 'entidades/oficio_list.html', {'oficios': oficios})

=======
            return redirect(reverse('trabajorealizado-list'))
    else:
        form = TrabajoRealizadoForm(instance=trabajo) 
        
    return render(request, 'trabajorealizado_form.html', {'form': form, 'titulo': f'Editar Trabajo ID: {trabajo.id}'})

#Crear Nuevo Oficio
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
def crear_oficio(request):
    if request.method == 'POST':
        form = OficioForm(request.POST) 
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:oficio-list'))
    else:
        form = OficioForm() 
    return render(request, 'entidades/oficio_form.html', {'form': form, 'titulo': 'Crear Nuevo Oficio'})
=======
            return redirect(reverse('oficio-list'))
    else:
        form = OficioForm() 
    return render(request, 'oficio_form.html', {'form': form, 'titulo': 'Crear Nuevo Oficio'})
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5

#Editar Oficio Existente
def editar_oficio(request, pk):
    oficio = get_object_or_404(oficio, pk=pk)
    
    if request.method == 'POST':
        form = OficioForm(request.POST, instance=oficio)
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:oficio-list'))
    else:
        form = OficioForm(instance=oficio) 
        
    return render(request, 'entidades/oficio_form.html', {'form': form, 'titulo': f'Editar Oficio: {oficio.nombre}'})

#Crear comentario para Trabajo Realizado

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'entidades/comentario_list.html', {'comentarios': comentarios})

=======
            return redirect(reverse('oficio-list'))
    else:
        form = OficioForm(instance=oficio) 
        
    return render(request, 'oficio_form.html', {'form': form, 'titulo': f'Editar Oficio: {oficio.nombre}'})

#Crear comentario para Trabajo Realizado
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST) 
        if form.is_valid():
            form.save() 
<<<<<<< HEAD
            return redirect(reverse('arreglatodo:comentario-list'))
    else:
        form = ComentarioForm() 
        
    return render(request, 'entidades/comentario_form.html', {'form': form, 'titulo': 'Agregar Comentario'})
=======
            return redirect(reverse('trabajorealizado-list'))
    else:
        form = ComentarioForm() 
        
    return render(request, 'comentario_form.html', {'form': form, 'titulo': 'Agregar Comentario'})
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
