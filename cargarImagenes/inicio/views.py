from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prueba_view(request):
    context = {}
    return render(request, 'imagenes/prueba.html', context)

def otra_view(request):
    return HttpResponse("Esta es otra vista")

