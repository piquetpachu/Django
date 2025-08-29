from django.contrib import admin
from .models import Ejercicio

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'grupo_muscular')
    list_filter = ('tipo', 'grupo_muscular')
    search_fields = ('nombre', 'grupo_muscular')
