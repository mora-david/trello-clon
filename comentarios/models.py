from django.db import models
from cards.models import Tarjeta
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Comentario(models.Model):
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE, related_name='tarjeta')
    mensaje = models.CharField(max_length=200)
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comdueño')
    fecha_creacion = models.DateField(default=timezone.now())
