from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'edad', 'sexo', 'peso_actual', 'altura', 'objetivo')
    search_fields = ('usuario__username', 'objetivo')
