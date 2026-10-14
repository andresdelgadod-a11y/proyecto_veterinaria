from django.db import models

class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre