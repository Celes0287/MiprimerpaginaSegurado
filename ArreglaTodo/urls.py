from django.contrib import admin
from django.urls import path, include
from MiprimerpaginaSegurado.views import * 
from ArreglaTodo import views
from .views import *

app_name = 'arreglatodo'

urlpatterns = [
    path('', home, name='home'),
    path('bienvenida_tpl/<str:nombre>/<str:apellido>/', bienvenida_tpl),
    path('saluda/', saluda),

    #Usuarios
    path('usuarios/', usuario, name='usuario-list'),
    path('usuarios/crear/', views.crear_usuario, name='usuario-crear'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='usuario-editar'),

    #Clientes
    path('clientes/', listar_clientes, name='cliente-list'),
    path('clientes/crear/', views.crear_cliente, name='cliente-crear'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='cliente-editar'),

    #Trabajos Pedidos
    path('trabajos_pedidos/', listar_trabajo_pedido, name='trabajo-pedido-list'),
    path('trabajos_pedidos/crear/', views.crear_trabajo_pedido, name='trabajo-pedido-crear'),
    path('trabajos_pedidos/editar/<int:pk>/', views.editar_trabajo_pedido, name='trabajo-pedido-editar'),

    #Trabajos Realizados
    path('trabajos_realizados/', listar_trabajos_realizados, name='trabajo-realizado-list'),
    path('trabajos_realizados/crear/', views.crear_trabajo_realizado, name='trabajo-realizado-crear'),
    path('trabajos_realizados/editar/<int:pk>/', views.editar_trabajo_realizado, name='trabajo-realizado-editar'),

    #Oficios
    path('oficios/', listar_oficios, name='oficio-list'),
    path('oficios/crear/', views.crear_oficio, name='oficio-crear'),
    path('oficios/editar/<int:pk>/', views.editar_oficio, name='oficio-editar'),

    # Comentarios
    path('comentarios/', listar_comentarios, name='comentario-list'),
    path('comentarios/crear/', views.crear_comentario, name='comentario-crear')
]
