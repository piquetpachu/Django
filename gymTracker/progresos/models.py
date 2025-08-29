from django.db import models
from django.conf import settings

class Progreso(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progresos'
    )
    fecha = models.DateField(auto_now_add=True)
    peso = models.FloatField(null=True, blank=True)
    grasa_corporal = models.FloatField(null=True, blank=True)
    medida_cintura = models.FloatField(null=True, blank=True)
    medida_brazo = models.FloatField(null=True, blank=True)
    medida_pierna = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha}"
