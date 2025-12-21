from django.db import models

# Create your models here.
class Oficio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

<<<<<<< HEAD
    class Meta:
        verbose_name = "Oficio"
        verbose_name_plural = "Oficios"
        ordering = ['nombre']
        
=======
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
<<<<<<< HEAD
    oficios = models.ManyToManyField(Oficio, help_text="Selecciona los oficios que realiza este usuario.")
    matricula = models.CharField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Prestador"
        verbose_name_plural = "Prestadores"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Matrícula: {self.matricula}"
=======
    contraseña = models.CharField(max_length=100)
    oficios = models.ManyToManyField(Oficio, help_text="Selecciona los oficios que realiza este usuario.")
    matricula = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nombre
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

<<<<<<< HEAD
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido}{self.telefono}"
=======
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
        
class Trabajo_pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')
    fecha_acordada = models.DateField(help_text="Fecha acordada para la realización del trabajo.")
<<<<<<< HEAD

    class Meta:
        verbose_name = "Trabajo Pedido"
        verbose_name_plural = "Trabajos Pedidos"
=======
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
    
    def __str__(self):
        return f"Trabajo pedido por {self.cliente.nombre} el {self.fecha_acordada} - {self.descripcion[:50]}..."

class Trabajo_realizado(models.Model):
    trabajo_pedido = models.ForeignKey(Trabajo_pedido, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    realizado = models.BooleanField(default=False) 

<<<<<<< HEAD
    class Meta:
        verbose_name = "Trabajo Realizado"
        verbose_name_plural = "Trabajos Realizados"

=======
>>>>>>> ee53445e159c7670bfa84756f7d045e7f643c4d5
    def __str__(self):
        if self.trabajo_pedido:
            return f"Trabajo Realizado - ID: {self.trabajo_pedido.id} - Completado: {self.realizado}"
        return f"Trabajo realizado para {self.trabajo_pedido.cliente.nombre} el {self.fecha_realizacion}"
    
class Comentario(models.Model):
    trabajo_realizado = models.ForeignKey(Trabajo_realizado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.nombre} en {self.trabajo_realizado.id} - {self.texto[:50]}..."
    

