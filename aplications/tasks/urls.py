from django.contrib import admin
from django.urls import path
from .views import registro, cerrarSesion, logear, inicio

urlpatterns = [
    path('', inicio, name='inicio' ),
    path('registro/', registro.as_view(), name='registro' ),
    path('cerrar_sesion/', cerrarSesion, name="cerrar_sesion"),
    path('logear/', logear, name="logear"),
]
