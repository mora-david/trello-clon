from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from listas.serializers import ListaSerializer
from listas.models import Lista


class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
