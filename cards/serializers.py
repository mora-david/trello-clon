from rest_framework import serializers
from cards.models import Tarjeta
from core.serializers import UserSerializer


class CardSerializer(serializers.ModelSerializer):
    """
    General purpose Card serializer
    """

    dueño = UserSerializer(read_only=True)
    miembros = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Tarjeta
        fields = ('nombre', 'miembros', 'lista', 'descripcion', 'dueño')


class CreateCardSerializer(serializers.ModelSerializer):
    """
    Create Card Serializer
    """
    class Meta:
        model = Tarjeta
        fields = (
            'nombre', 'lista', 'descripcion', 'miembros', 'dueño', 'fecha_creacion', 'fecha_vencimiento', 'posicion')
