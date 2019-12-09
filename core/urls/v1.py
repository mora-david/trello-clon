from rest_framework import routers
from django.urls import path, include

from core.views import UserViewSet
from tableros.views import TableroViewSet
from listas.views import ListaViewSet
from cards.views import CardViewSet
from comentarios.views import ComentarioViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'tableros', TableroViewSet)
routers.register(r'listas', ListaViewSet)
routers.register(r'tarjetas', CardViewSet)
routers.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
