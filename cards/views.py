from rest_framework import viewsets, status, authentication

from cards.models import Tarjeta
from cards.serializers import CardSerializer, CreateCardSerializer, CardSerializer1111



from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CardViewSet(viewsets. ModelViewSet):
    queryset = Tarjeta.objects.all().order_by('fecha_creacion')
    serializer_class = CardSerializer


    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            return CreateCardSerializer
        else:
            return CardSerializer

class Card1111(viewsets. ModelViewSet):
    queryset = Tarjeta.objects.all().order_by('-id')[:1]


    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return CardSerializer1111



