from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ejercicios.models import Ejercicio

def inicio(request):
    ejercicios = Ejercicio.objects.all()
    ejercicios_list = ', '.join([str(ejercicio) for ejercicio in ejercicios])
    ejercicio_id = request.GET.get('edit')
    update_ejercicio = None
    if ejercicio_id:
        try:
            update_ejercicio = Ejercicio.objects.get(id=ejercicio_id)
        except Ejercicio.DoesNotExist:
            pass

    context = {
        'ejercicios': ejercicios, 
        'ejercicios_list': ejercicios_list,
        'update': update_ejercicio
    }
    return render(request, 'ejercicios/index.html', context)

def eliminar(request, id):
    if request.method == 'POST':
        try:
            ejercicio = Ejercicio.objects.get(id=id)
            ejercicio.delete()
            print(f"Ejercicio con id {id} eliminado")
            return redirect("ejercicios:index")
        except Exception as e:
            print(f"Error: {e}")
            return redirect("ejercicios:index")
    else:
        return redirect("ejercicios:index")

def update(request, id):
    if request.method == 'POST':
        try:
            ejercicio = get_object_or_404(Ejercicio, id=id)
            ejercicio.nombre = request.POST["nombre"]
            ejercicio.tipo = request.POST["tipo"]
            ejercicio.grupo_muscular = request.POST.get("grupo_muscular", "")
            ejercicio.descripcion = request.POST.get("descripcion", "")
            ejercicio.video_url = request.POST.get("video_url", "")
            ejercicio.save()
            print(f"Ejercicio con id {id} actualizado")
        except Exception as e:
            print(f"Error: {e}")
    return redirect("ejercicios:index")

def insert(request):
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            tipo = request.POST['tipo']
            grupo_muscular = request.POST.get('grupo_muscular', '')
            descripcion = request.POST.get('descripcion', '')
            video_url = request.POST.get('video_url', '')
            
            if not nombre or not tipo:
                raise ValueError("Nombre y tipo son requeridos")
            
            ejercicio = Ejercicio(
                nombre=nombre,
                tipo=tipo,
                grupo_muscular=grupo_muscular,
                descripcion=descripcion,
                video_url=video_url
            )
            ejercicio.save()
            print(f"Ejercicio {nombre} creado exitosamente")
        except Exception as e:
            print(f"Error: {e}")
    return redirect("ejercicios:index")