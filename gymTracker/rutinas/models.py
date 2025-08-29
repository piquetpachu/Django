
from django.db import models
from django.conf import settings

class Rutina(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rutinas'
    )
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.usuario.username})"


class DiaRutina(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='dias')
    nombre_dia = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre_dia} - {self.rutina.nombre}"


class DiaEjercicio(models.Model):
    dia = models.ForeignKey(DiaRutina, on_delete=models.CASCADE, related_name='ejercicios')
    ejercicio = models.ForeignKey('ejercicios.Ejercicio', on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('dia', 'ejercicio')
        ordering = ['orden']

    def __str__(self):
        return f"{self.ejercicio.nombre} en {self.dia.nombre_dia}"
