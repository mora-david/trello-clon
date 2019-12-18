from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from listas.models import Lista
from listas.serializers import ListaSerializer
from tableros.serializers import TableroSerializer


class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

    @action(detail=True, methods=['GET', 'POST'])
    def board(self, request, pk=None):
        lista = self.get_object()
        board = lista.tablero
        serializer = TableroSerializer(board)
        return Response(status=status.HTTP_200_OK, data=serializer.data)