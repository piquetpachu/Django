from django.contrib import admin
from .models import RegistroEntrenamiento, SerieDetalle

@admin.register(RegistroEntrenamiento)
class RegistroEntrenamientoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ejercicio', 'fecha', 'series', 'repeticiones', 'peso_usado')
    list_filter = ('fecha', 'usuario')
    search_fields = ('ejercicio__nombre', 'usuario__username')

@admin.register(SerieDetalle)
class SerieDetalleAdmin(admin.ModelAdmin):
    list_display = ('registro', 'nro_serie', 'repeticiones', 'peso')
    list_filter = ('registro',)
