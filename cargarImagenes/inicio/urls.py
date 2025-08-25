from django.urls import  path
from . import views

urlpatterns = [
    path('', views.prueba_view, name='prueba'),
    path('otra/', views.otra_view, name='otra'),
]