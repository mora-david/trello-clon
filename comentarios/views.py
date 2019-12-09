from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer, CreateComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            return CreateComentarioSerializer
        else:
            return ComentarioSerializer
        return ComentarioSerializer