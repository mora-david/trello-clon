from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions

from core.serializers import UserSerializer
from django.http import HttpResponse, HttpResponseRedirect

from tableros.models import Tablero
from listas.models import Lista
from tableros.serializers import TableroSerializer, CreateTableroSerializer
from listas.serializers import ListaSerializer


class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            user = self.request.user
            if Tablero.dueño == 0:
                Tablero.dueño = user
            return CreateTableroSerializer
        else:
            return TableroSerializer
        return TableroSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        if self.request.user.is_staff:
            return Tablero.objects.all()
        else:
            user = self.request.user
            return Tablero.objects.filter(dueño=user).order_by('-id')[:1]



    """
    @action(detail=True, methods=['GET'])
    def dueño(self, request, pk=None):
        tablero = self.get_object()
        usuario = tablero.dueño
        serializer = UserSerializer(usuario)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

"""

    @action(detail=True, methods=['GET', 'POST'])
    def dueño(self, request, pk=None):
        tablero = self.get_object()
        usuario = tablero.dueño
        serializer = UserSerializer(usuario)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=True, methods=['GET', 'POST'])
    def fav(self, request, pk=None):
        tablero1 = self.get_object()
        lst = Lista.objects.filter(tablero_id=tablero1.id)
        serializer = ListaSerializer(lst, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
