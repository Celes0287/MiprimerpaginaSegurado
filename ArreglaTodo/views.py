from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import Q


# HOME
def home(request):
    return render(request, 'entidades/index.html')

# Usuario
@login_required
def usuario(request):
    try:
        usuario = Usuario.objects.get(email=request.user.email)
    except Usuario.DoesNotExist:
        usuario = None

    contexto = {"usuario": usuario,}
    return render(request, 'entidades/usuario_list.html', contexto)

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:usuario-list'))
    else:
        form = UsuarioForm() 
            
    return render(request, 'entidades/usuario_form.html', {'form': form, 'titulo': 'Crear Usuario'})

# Editar Usuario Existente
@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:usuario-list'))
    else:
        form = UsuarioForm(instance=usuario) 
        
    return render(request, 'entidades/usuario_form.html', {'form': form, 'titulo': f'Editar Usuario: {usuario.nombre}'})

# Cliente
@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'entidades/cliente_list.html', {'clientes': clientes})

# Crear Nuevo Cliente
@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:cliente-list'))
    else:
        form = ClienteForm() 
        
    return render(request, 'entidades/cliente_form.html', {'form': form, 'titulo': 'Crear Cliente'})


# Editar Cliente Existente
@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:cliente-list'))
    else:
        form = ClienteForm(instance=cliente) 
        
    return render(request, 'entidades/cliente_form.html', {'form': form, 'titulo': f'Editar Cliente: {cliente.nombre}'})

# Trabajo Pedido
@login_required
def listar_trabajo_pedido(request):
    trabajos_pedidos = Trabajo_pedido.objects.all()
    return render(request, 'entidades/trabajo_pedido_list.html', {'trabajo_pedido': trabajos_pedidos})

# Crear Nuevo Trabajo Pedido
@login_required
def crear_trabajo_pedido(request):
    if request.method == 'POST':
        form = TrabajoPedidoForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:trabajo-pedido-list'))
    else:
        form = TrabajoPedidoForm() 
        
    return render(request, 'entidades/trabajo_pedido_form.html', {'form': form, 'titulo': 'Crear Pedido'})

# Editar Trabajo Pedido Existente
@login_required
def editar_trabajo_pedido(request, pk):
    trabajo = get_object_or_404(Trabajo_pedido, pk=pk)
    
    if request.method == 'POST':
        form = TrabajoPedidoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:trabajo-pedido-list'))
    else:
        form = TrabajoPedidoForm(instance=trabajo) 
        
    return render(request, 'entidades/trabajo_pedido_form.html', {'form': form, 'titulo': f'Editar Pedido para Cliente: {trabajo.cliente.nombre}'})

# Trabajo Realizado
@login_required
def listar_trabajos_realizados(request):
    trabajos_realizados = Trabajo_realizado.objects.all()
    return render(request, 'entidades/trabajo_realizado_list.html', {'trabajos_realizados': trabajos_realizados})

# Registrar Trabajo Realizado
@login_required
def crear_trabajo_realizado(request):
    if request.method == 'POST':
        form = TrabajoRealizadoForm(request.POST) 
        if form.is_valid():
            form.save() 

            return redirect(reverse('arreglatodo:trabajo-realizado-list'))
    else:
        form = TrabajoRealizadoForm() 
        
    return render(request, 'entidades/trabajo_realizado_form.html', {'form': form})


#Editar Trabajo Realizado
@login_required
def editar_trabajo_realizado(request, pk):
    trabajo = get_object_or_404(Trabajo_realizado, pk=pk)
    
    if request.method == 'POST':
        form = TrabajoRealizadoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:trabajo-realizado-list'))
    else:
        form = TrabajoRealizadoForm(instance=trabajo) 
        
    return render(request, 'entidades/trabajo_realizado_form.html', {'form': form, 'titulo': f'Editar Trabajo ID: {trabajo.id}'})

#Oficio
@login_required
def listar_oficios(request):
    oficios = Oficio.objects.all()
    return render(request, 'entidades/oficio_list.html', {'oficios': oficios})

#Crear Nuevo Oficio
@login_required
def crear_oficio(request):
    if request.method == 'POST':
        form = OficioForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:oficio-list'))
    else:
        form = OficioForm() 
    return render(request, 'entidades/oficio_form.html', {'form': form, 'titulo': 'Crear Nuevo Oficio'})



#Editar Oficio Existente
@login_required
def editar_oficio(request, pk):
    oficio = get_object_or_404(oficio, pk=pk)
    
    if request.method == 'POST':
        form = OficioForm(request.POST, instance=oficio)
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:oficio-list'))
    else:
        form = OficioForm(instance=oficio) 
        
    return render(request, 'entidades/oficio_form.html', {'form': form, 'titulo': f'Editar Oficio: {oficio.nombre}'})

#Crear comentario para Trabajo Realizado
@login_required
def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'entidades/comentario_list.html', {'comentarios': comentarios})


#Crear comentario para Trabajo Realizado
@login_required
def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect(reverse('arreglatodo:comentario-list'))
    else:
        form = ComentarioForm() 
        
    return render(request, 'entidades/comentario_form.html', {'form': form, 'titulo': 'Agregar Comentario'})

# Buscar Clientes
@login_required
def buscar_clientes(request):
    return render(request, 'entidades/buscar_cliente.html')

# Encontrar Clientes
@login_required
def encontrar_clientes(request):
    if request.GET["Buscar"]:
        patron = request.GET["Buscar"]
        clientes = Cliente.objects.filter(clientes = Cliente.objects.filter(
            Q(nombre__icontains=patron) |
            Q(apellido__icontains=patron) |
            Q(email__icontains=patron) |
            Q(telefono__icontains=patron)
        ))
        contexto = {"clientes": clientes, "patron": patron}
        return render(request, 'entidades/encontrar_cliente.html', contexto) 
    else:
        mensaje = "No se ingresó ningún término de búsqueda."
        return render(request, 'entidades/cliente_list.html', {"mensaje": mensaje}) #cliente_list porque es el que muestra todos los clientes


#Login / Logout / Registrarse

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    #fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('arreglatodo:home')
    
#Registrar usuario
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('arreglatodo:home')
    else:
        form = RegistroForm()
    
    return render(request, 'registration/register.html', {'form': form})

#Sobre Nosotros
def sobre_nosotros(request):
    return render(request, 'entidades/sobre_nosotros.html')
