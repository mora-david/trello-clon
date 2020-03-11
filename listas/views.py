from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser


from listas.models import Lista
from tableros.models import Tablero
from listas.serializers import ListaSerializer
from tableros.serializers import TableroSerializer


class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                return Lista.objects.all()
            else:
                user = self.request.user
                tablero1 = Tablero.objects.filter(dueño=user)[:1]
                return Lista.objects.filter(tablero=tablero1)


    @action(detail=True, methods=['GET', 'POST'])
    def board(self, request, pk=None):
        lista = self.get_object()
        board = lista.tablero
        serializer = TableroSerializer(board)
        return Response(status=status.HTTP_200_OK, data=serializer.data)