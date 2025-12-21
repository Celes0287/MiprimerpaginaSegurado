from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Trabajo_pedido)
admin.site.register(Trabajo_realizado)
admin.site.register(Oficio)
admin.site.register(Comentario)