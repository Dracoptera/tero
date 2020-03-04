from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    tel = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    # Clase para mostrar el nombre en la tabla desde el panel de admin.
    def __str__(self):
        return self.nombre 

class Medicamento(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    dosis = models.FloatField(null=True)
    cantidad = models.FloatField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

class Alarma(models.Model):
    #usuario = 
    #medicamento = 
    estado = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    