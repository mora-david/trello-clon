from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from listas.models import Lista


class Tarjeta(models.Model):
    nombre = models.CharField(max_length=100)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    miembros = models.ManyToManyField(User, related_name='tmiembros')
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tdueño')
    fecha_creacion = models.DateField(default=timezone.now())
    fecha_vencimiento = models.DateField(null=True)
    posicion = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.posicion:
            self.posicion = Tarjeta.objects.all().count() + 1
        super(Tarjeta, self).save(*args, **kwargs)
