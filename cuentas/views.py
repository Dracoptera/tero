from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MedicamentoForm, AlarmaForm

# Create your views here.
from .models import *


def index(request):
    usuario = Usuario.objects.get(id=1)
    return render(request, 'cuentas/dashboard.html', {'usuario': usuario})


def medicamentos(request):
    med_form = MedicamentoForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        med_form = MedicamentoForm(request.POST)
        if med_form.is_valid():
            med_form.save()

    medicamentos = Medicamento.objects.all()
    usuario = Usuario.objects.get(id=1)

    contexto = {'medicamentos': medicamentos,
                'usuario': usuario, 'med_form': med_form}

    return render(request, 'cuentas/medicamentos.html', contexto)


def medicamento(request, pk_med):
    medicamentos = Medicamento.objects.all()
    medicamento = Medicamento.objects.get(id=pk_med)
    usuario = Usuario.objects.get(id=1)

    med_form = MedicamentoForm(instance=medicamento)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        med_form = MedicamentoForm(request.POST, instance=medicamento)
        if med_form.is_valid():
            med_form.save()

    contexto = {'medicamento': medicamento, 'medicamentos': medicamentos,
                'usuario': usuario, 'med_form': med_form}
    return render(request, 'cuentas/medicamento.html', contexto)


def eliminar(request, pk_med):
    medicamento = Medicamento.objects.get(id=pk_med)
    del_form = MedicamentoForm(instance=medicamento)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('/medicamentos/')

    contexto = {'medicamento': medicamento, 'del_form': del_form}
    return render(request, 'cuentas/eliminar.html', contexto)


def usuario(request):
    medicamentos = Medicamento.objects.all()
    usuario = Usuario.objects.get(id=1)
    return render(request, 'cuentas/usuario.html', {'medicamentos': medicamentos, 'usuario': usuario})


def alarmas(request):
    alarma_form = AlarmaForm()
    if request.method == 'POST':
        alarma_form = AlarmaForm(request.POST)
        if alarma_form.is_valid():
            alarma_form.save()

    medicamentos = Medicamento.objects.all()
    usuario = Usuario.objects.get(id=1)
    alarmas = Alarma.objects.all()
    contexto = {'medicamentos': medicamentos,
                'usuario': usuario, 'alarma_form': alarma_form, 'alarmas': alarmas}

    return render(request, 'cuentas/alarmas.html', contexto)


def agenda(request):

    return render(request, 'cuentas/agenda.html')
