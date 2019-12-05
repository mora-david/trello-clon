from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tableros.models import Tablero
from tableros.serializers import TableroSerializer, CreateTableroSerializer


class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            return CreateTableroSerializer
        else:
            return TableroSerializer
        return TableroSerializer