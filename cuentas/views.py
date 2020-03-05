from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import * 

def index(request): 
    usuario = Usuario.objects.get(id=1)
    return render(request, 'cuentas/dashboard.html', {'usuario': usuario})

def medicamentos(request):
    medicamentos = Medicamento.objects.all()
    usuario = Usuario.objects.get(id=1)
    return render(request, 'cuentas/medicamentos.html', {'medicamentos': medicamentos})

def usuario(request):
    medicamentos = Medicamento.objects.all()
    usuario = Usuario.objects.get(id=1)
    return render(request, 'cuentas/usuario.html', {'medicamentos': medicamentos, 'usuario': usuario})

def alarmas(request):
    return render(request, 'cuentas/alarmas.html')

def agenda(request): 
    return render(request, 'cuentas/agenda.html')