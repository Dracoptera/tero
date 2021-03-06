from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MedicamentoForm, AlarmaForm, UsuarioForm

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


def perfil(request):
    usuario = Usuario.objects.get(id=1)

    usuario_form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()

    contexto = {
        'usuario': usuario, 'usuario_form': usuario_form}
    return render(request, 'cuentas/perfil.html', contexto)


def alarmas(request):
    alarma_form = AlarmaForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        alarma_form = AlarmaForm(request.POST)
        if alarma_form.is_valid():
            alarma_form.save()

    alarmas = Alarma.objects.all()
    usuario = Usuario.objects.get(id=1)

    contexto = {'alarmas': alarmas, 'alarma_form': alarma_form}

    return render(request, 'cuentas/alarmas.html', contexto)


def alarma(request, pk_al):
    alarmas = Alarma.objects.all()
    alarma = Alarma.objects.get(id=pk_al)

    alarma_form = AlarmaForm(instance=alarma)
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        alarma_form = AlarmaForm(request.POST, instance=alarma)
        if alarma_form.is_valid():
            alarma_form.save()

    contexto = {'alarmas': alarmas, 'alarma': alarma,
                'alarma_form': alarma_form}
    return render(request, 'cuentas/alarma.html', contexto)


def eliminar_al(request, pk_al):
    alarma = Alarma.objects.get(id=pk_al)
    del_form = AlarmaForm(instance=alarma)

    if request.method == 'POST':
        alarma.delete()
        return redirect('/alarmas/')

    contexto = {'alarma': alarma, 'del_form': del_form}
    return render(request, 'cuentas/eliminar_al.html', contexto)


def agenda(request):
    return render(request, 'cuentas/agenda.html')


def test(request):
    return HttpResponse("Done!")
