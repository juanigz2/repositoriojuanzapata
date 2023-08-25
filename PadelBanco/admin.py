from django.contrib import admin
from .models import Turnos, Profesores, Alumnos

# Register your models here.

admin.site.register(Turnos)
admin.site.register(Profesores)
admin.site.register(Alumnos)
