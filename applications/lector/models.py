from django.db import models

# Create your models here.
from applications.libro.models import Libro

class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.nombre + " " + self.apellido

class Prestamos(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField("Fecha de prestamo")
    fecha_devolucion = models.DateField(blank=True, null=False)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return self.lector.nombre + " " + self.lector.apellido + " " + self.libro.titulo
