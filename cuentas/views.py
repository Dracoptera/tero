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
    contexto = {'medicamentos': medicamentos, 'usuario': usuario}

    return render(request, 'cuentas/medicamentos.html', contexto)

def medicamento(request, pk_med):
    medicamentos = Medicamento.objects.all()
    medicamento = Medicamento.objects.get(id=pk_med)
    usuario = Usuario.objects.get(id=1)

    contexto = {'medicamento': medicamento, 'medicamentos': medicamentos, 'usuario': usuario}
    return render(request, 'cuentas/medicamento.html', contexto)

def usuario(request):
    medicamentos = Medicamento.objects.all()
    usuario = Usuario.objects.get(id=1)
    return render(request, 'cuentas/usuario.html', {'medicamentos': medicamentos, 'usuario': usuario})

def alarmas(request):
    return render(request, 'cuentas/alarmas.html')

def agenda(request): 
    return render(request, 'cuentas/agenda.html')