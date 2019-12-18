from rest_framework import serializers
from tableros.models import Tablero
from core.serializers import UserSerializer


class TableroSerializer(serializers.ModelSerializer):
    """
    General purpose Tablero serializer
    """

    dueño = UserSerializer(read_only=True)
    favorito = UserSerializer(many=True, read_only=True)
    miembros = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Tablero
        fields = ('id','nombre', 'descripcion', 'fecha_de_creacion', 'dueño', 'favorito', 'miembros')


class CreateTableroSerializer(serializers.ModelSerializer):
    """
    Create Tablero serializer
    """

    class Meta:
        model = Tablero
        fields = ('nombre', 'descripcion', 'fecha_de_creacion', 'dueño', 'favorito', 'miembros')
