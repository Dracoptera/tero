from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): 
    return render(request, 'cuentas/dashboard.html')

def medicamentos(request):
    return render(request, 'cuentas/medicamentos.html')

def usuario(request):
    return render(request, 'cuentas/usuario.html')

def alarmas(request):
    return render(request, 'cuentas/alarmas.html')

def agenda(request): 
    return render(request, 'cuentas/agenda.html')