from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('update/<int:tarea_id>/', views.update_form, name='update_form'),
    path('borrar/<int:tarea_id>/', views.borrar, name='borrar'),
]
