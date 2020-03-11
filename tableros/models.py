from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

VISIBILIDAD = (
    ('V', 'Visible'),
    ('N', 'No visible'),
)


class Tablero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_de_creacion = models.DateField(default=timezone.now())
    dueño = models.ForeignKey(User, related_name='dueño', blank=True, null=True, on_delete=models.CASCADE)
    favorito = models.ManyToManyField(User, related_name='favorito')
    visibilidad = models.CharField(max_length=1, choices=VISIBILIDAD)
    miembros = models.ManyToManyField(User, related_name='miembros')



    def __str__(self):
        return self.nombre
