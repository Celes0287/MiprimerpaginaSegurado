from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'matricula', 'user')
    fields = ('user', 'nombre', 'apellido', 'telefono', 'email', 'oficios', 'matricula')

admin.site.register(Cliente)
admin.site.register(Trabajo_pedido)
admin.site.register(Trabajo_realizado)
admin.site.register(Oficio)
admin.site.register(Comentario)
admin.site.register(Profile)
