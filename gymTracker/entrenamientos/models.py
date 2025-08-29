from django.db import models
from django.conf import settings

class RegistroEntrenamiento(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registros'
    )
    ejercicio = models.ForeignKey('ejercicios.Ejercicio', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    series = models.PositiveIntegerField(null=True, blank=True)
    repeticiones = models.PositiveIntegerField(null=True, blank=True)
    peso_usado = models.FloatField(null=True, blank=True)
    tiempo = models.FloatField(null=True, blank=True, help_text='Minutos (para cardio)')

    def __str__(self):
        return f"{self.usuario.username} - {self.ejercicio.nombre} - {self.fecha}"


class SerieDetalle(models.Model):
    registro = models.ForeignKey(RegistroEntrenamiento, on_delete=models.CASCADE, related_name='series_detalle')
    nro_serie = models.PositiveIntegerField()
    repeticiones = models.PositiveIntegerField()
    peso = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['nro_serie']

    def __str__(self):
        return f"Serie {self.nro_serie} - {self.registro.ejercicio.nombre}"
