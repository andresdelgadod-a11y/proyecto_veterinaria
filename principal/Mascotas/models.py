from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.PositiveIntegerField()
    dueno = models.ForeignKey('duenos.Dueno', on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return self.nombre
