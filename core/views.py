from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

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

    """def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [AllowAny, ]
        return [permission() for permission in permission_classes]
"""
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer
