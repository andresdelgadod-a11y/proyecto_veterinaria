from django.db import models

class Cita(models.Model):
    # Cada cita pertenece a una mascota (relación con la app Mascotas)
    mascota = models.ForeignKey('Mascotas.Mascota', on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, default='pendiente')

    def _str_(self):
        return f'{self.mascota} - {self.fecha:%Y-%m-%d %H:%M}'