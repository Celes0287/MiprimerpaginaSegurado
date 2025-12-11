from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def saluda(request):
    return HttpResponse("Hola Django - MiprimerpaginaSegurado")

def bienvenida_tpl(request, nombre, apellido):
    hoy = datetime.datetime.now()
    contexto = ({"nombre": nombre, "apellido": apellido, "hoy": hoy})
    plantilla = loader.get_template('bienvenida.html')
    respuesta = plantilla.render(contexto)
    
    return HttpResponse(respuesta)