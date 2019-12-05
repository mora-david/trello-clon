from rest_framework import serializers
from listas.models import Lista
from tableros.serializers import TableroSerializer


class ListaSerializer(serializers.ModelSerializer):
    """
    General Purpose Serializer
    """

    class Meta:
        model = Lista
        fields = ('nombre', 'tablero', 'fecha_creacion', 'posicion')
