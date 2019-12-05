from rest_framework import routers
from django.urls import path, include

from core.views import UserViewSet
from tableros.views import TableroViewSet
from listas.views import ListaViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'tableros', TableroViewSet)
routers.register(r'Listas', ListaViewSet)

urlpatterns = [
    path('', include(routers.urls))
]