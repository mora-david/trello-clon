from rest_framework import serializers
from comentarios.models import Comentario
from core.serializers import UserSerializer
from cards.serializers import CardSerializer


class ComentarioSerializer(serializers.ModelSerializer):
    """
    General purpose Comentario serializer
    """

    dueño = UserSerializer(read_only=True)
    tarjeta = CardSerializer

    class Meta:
        model = Comentario
        fields = ('tarjeta', 'mensaje', 'dueño', 'fecha_creacion')


class CreateComentarioSerializer(serializers.ModelSerializer):
    """
    Create purpose Comentario serializer
    """

    class Meta:
        model = Comentario
        fields = ('tarjeta', 'mensaje', 'dueño', 'fecha_creacion')
