from django.db import models
from django.contrib.auth.models import User

class Videojuego(models.Model):
    videojuegosSeleccion = (
    ('accion', 'Acción'),
    ('aventura','Aventura'),
    ('estrategia','Estrategia'),
    ('rol','Rol'),
    ('simulacion','Simulación'),
    ('otro','Otro')
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=45)
    genero = models.CharField(max_length=15, choices=videojuegosSeleccion)
    creador = models.CharField(max_length=30)
    descripcion = models.TextField(null=True, blank=True)
    lanzamiento = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenVideojuego = models.ImageField(null=True, blank=True, upload_to="assets/")

    def __str__(self):
        return f'{self.nombre} by {self.creador}'

class Comentario(models.Model):
    comentario = models.ForeignKey(Videojuego, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)