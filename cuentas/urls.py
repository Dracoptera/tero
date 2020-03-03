from django.urls import path
from . import views # importa views de la base 

urlpatterns = [
    path('', views.index),
    path('medicamentos/', views.medicamentos),
    path('usuario/', views.usuario),
    path('alarmas/', views.alarmas),
    path('agenda/', views.agenda),
]