from django.db import models
from tableros.models import Tablero
from django.utils import timezone


# Create your models here.


class Lista(models.Model):
    nombre = models.CharField(max_length=100)
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now())
    posicion = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.posicion:
            self.posicion = Lista.objects.all().count() + 1
        super(Lista, self).save(*args, **kwargs)
