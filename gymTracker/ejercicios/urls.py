from django.urls import include, path

from . import views

app_name = 'ejercicios'

urlpatterns = [
    path('', views.inicio, name='index'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('update/<int:id>/', views.update, name='update'),
    path('insert/', views.insert, name='insert'),
]
