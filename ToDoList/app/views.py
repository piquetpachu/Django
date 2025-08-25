from django.shortcuts import redirect, render, HttpResponse
from .models import tareas
# Create your views here.
def inicio(request):
    tareas_list = tareas.objects.all()
    print(tareas_list)
    context = {
        "tareas": tareas_list[::-1]
    }
    return render(request, 'app/index.html', context)

def insert(request):
    try:
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        if not titulo or not descripcion:
            raise ValueError("Titulo y descripcion son requeridos")
        tarea_list = tareas(titulo=titulo, descripcion=descripcion)
        tarea_list.save()
        return redirect("inicio")
    except Exception as e:
        print(f"Error: {e}")
        return redirect("inicio")   

def update(request):
    tarea_id = request.POST["id"]
    task_subject = request.POST["titulo"]
    task_description = request.POST["descripcion"]
    tareas_list = tareas.objects.get(pk=tarea_id)
    tareas_list.titulo = task_subject
    tareas_list.descripcion = task_description
    tareas_list.save()
    return redirect("inicio")


def update_form(request, tarea_id):
    tareas_list = tareas.objects.all()
    tareas_list_only = tareas.objects.get(pk=tarea_id)
    print(tareas_list_only)
    context = {
        "tareas_list": tareas_list[::-1],
        "update": tareas_list_only
    }
    return render(request, "app/index.html", context)


def borrar(request, tarea_id):
    try:
        tarea = tareas.objects.get(id=tarea_id)
        tarea.delete()
        print(f"Tarea con id {tarea_id} eliminada")
        return redirect("inicio")
    except Exception as e:
        print(f"Error: {e}")
        return redirect("inicio")
