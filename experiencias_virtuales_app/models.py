from django.db import models

# Create your models here.


class Preferencia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class StarTalent(models.Model):
    nombre_experiencia = models.CharField(max_length=100)
    costo_experiencia = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre_experiencia


class Espectador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    presupuesto_dolares = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre

