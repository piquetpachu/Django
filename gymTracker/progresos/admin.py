from django.contrib import admin
from .models import Progreso

@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'peso', 'grasa_corporal', 'medida_cintura', 'medida_brazo', 'medida_pierna')
    list_filter = ('fecha', 'usuario')
    search_fields = ('usuario__username',)
