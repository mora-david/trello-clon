from django.db import models
from tableros.models import Tablero
from django.utils import timezone


# Create your models here.


class Lista(models.Model):
    nombre = models.CharField(max_length=100)
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=timezone.now())
    posicion = models.IntegerField(default=9999999999)

    def save(self, *args, **kwargs):
        if self.posicion == 9999999999:
            self.posicion = Lista.objects.all().count() + 1
            super(Lista, self).save(*args, **kwargs)
