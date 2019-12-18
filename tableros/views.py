from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from core.serializers import UserSerializer
from django.http import HttpResponse, HttpResponseRedirect

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

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        try:
            if self.request.user.username != 'dave':
                user = self.request.user
                return Tablero.objects.filter(dueño=user)
            else:
                return Tablero.objects.all()
        except:
            return Tablero.objects.all()



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

