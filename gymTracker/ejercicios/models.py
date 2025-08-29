from django.db import models

class Ejercicio(models.Model):
    TIPOS = [
        ('fuerza', 'Fuerza'),
        ('cardio', 'Cardio'),
        ('movilidad', 'Movilidad'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    grupo_muscular = models.CharField(max_length=50, blank=True)
    descripcion = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.grupo_muscular})"
