from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    tel = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    nacimiento = models.DateField(null=True)
    altura = models.FloatField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    # Clase para mostrar el nombre en la tabla desde el panel de admin.
    def __str__(self):
        return self.nombre 

class Medicamento(models.Model):
    TIPOS = (
        ('g', 'g'),
        ('mg', 'mg'),
        ('ml', 'ml'),
        ('Ul', 'Ul'),
        ('mcg', 'mcg'),
        ('mcg/ml', 'mcg/ml'),
        ('mEq', 'mEq'),
        ('%', '%'),
        ('mg/g', 'mg/g'),
        ('mg/cm2', 'mg/cm2'),
        ('mg/ml', 'mg/ml'),
        ('mcg/hora', 'mcg/hora'),
    )

    nombre = models.CharField(max_length=200, null=True)
    dosis = models.FloatField(null=True)
    tipo_dosis = models.CharField(max_length=200, null=True, choices=TIPOS)
    cantidad = models.IntegerField(null=True)
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.nombre 

class Alarma(models.Model):
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    medicamento = models.ForeignKey(Medicamento, null=True, on_delete=models.SET_NULL) 
    estado = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.medicamento 
    