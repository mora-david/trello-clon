from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from cards.models import Tarjeta
from cards.serializers import CardSerializer, CreateCardSerializer

class CardViewSet(viewsets. ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = CardSerializer

    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            return CreateCardSerializer
        else:
            return CardSerializer
        return CardSerializer
