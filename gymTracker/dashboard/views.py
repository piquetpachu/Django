from django.shortcuts import render
from ejercicios.models import Ejercicio
from entrenamientos.models import RegistroEntrenamiento
from progresos.models import Progreso
from rutinas.models import Rutina

def index(request):
    if request.user.is_authenticated:
        context = {
            "rutinas_count": Rutina.objects.filter(usuario=request.user).count(),
            "progresos_count": Progreso.objects.filter(usuario=request.user).count(),
            "entrenamientos_count": RegistroEntrenamiento.objects.filter(usuario=request.user).count(),
            "ejercicios_count": Ejercicio.objects.count(),
            "ultimos_progresos": Progreso.objects.filter(usuario=request.user).order_by('-fecha')[:5]
        }
    else:
        context = {
            "rutinas_count": 0,
            "progresos_count": 0,
            "entrenamientos_count": 0,
            "ejercicios_count": 0,
            "ultimos_progresos": []
        }
    return render(request, "dashboard/index.html", context)

