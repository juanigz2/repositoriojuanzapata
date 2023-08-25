from django.urls import path
from .views import *


urlpatterns = [
    path('crear_profe/', crear_profe),
    path('listar_profes/', listar_profes),
    path('turnos/', turnos, name="turnos"),
    path('profesores/', profesores, name="profesores"),
    path('alumnos/', alumnos, name="alumnos"),
    path('busquedaprofesor/', busquedaprofesor, name="busquedaprofesor"),
    path("buscar/", buscar, name="buscar"),
    
    ]