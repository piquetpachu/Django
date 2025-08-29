from django.contrib import admin
from .models import Rutina, DiaRutina, DiaEjercicio

@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', 'usuario__username')

@admin.register(DiaRutina)
class DiaRutinaAdmin(admin.ModelAdmin):
    list_display = ('nombre_dia', 'rutina')
    search_fields = ('nombre_dia', 'rutina__nombre')

@admin.register(DiaEjercicio)
class DiaEjercicioAdmin(admin.ModelAdmin):
    list_display = ('dia', 'ejercicio', 'orden')
    list_filter = ('dia',)
    search_fields = ('ejercicio__nombre',)
