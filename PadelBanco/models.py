from django.db import models

class Turnos(models.Model):
    nombre=models.CharField(max_length=50)
    horario=models.IntegerField()
    completado=models.BooleanField()
    def __str__(self):
        return f"{self.nombre} - {self.horario} - {self.completado}"

class Profesores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"

class Alumnos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"




