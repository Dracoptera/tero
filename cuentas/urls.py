from django.urls import path
from . import views # importa views de la base 

urlpatterns = [
    path('', views.index, name="home"),
    path('medicamentos/', views.medicamentos, name="medicamentos"),
    path('medicamento/<str:pk_med>/', views.medicamento, name="medicamento"),
    path('eliminar/<str:pk_med>/', views.eliminar, name="eliminar"),
    path('usuario/', views.usuario, name="usuario"),
    path('alarmas/', views.alarmas, name="alarmas"),
    path('agenda/', views.agenda, name="agenda"),
]