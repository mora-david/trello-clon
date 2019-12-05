from django.contrib.auth.models import User
from rest_framework import viewsets

from core.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Regresa la instancia de un usuario
    list:
    Regresa la lista de usuarios
    update:
    Actualiza un usuario
    partial update:
    Actualiza un campo en particular de un usuario
    delete:
    Elimina un Usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer
