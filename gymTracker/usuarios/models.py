from django.db import models
from django.conf import settings

class Perfil(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    edad = models.PositiveIntegerField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M','M'),('F','F'),('Otro','Otro')], blank=True)
    peso_actual = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    objetivo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - Perfil"
