from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from nomina.models import Departamento
from nomina.forms import DepartamentoForm


def departamento_list(request):
    departamentos = Departamento.objects.all()
    return render(request, 'nomina/departamentos/lista.html', {'departamentos': departamentos})


def departamento_detail(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    return render(request, 'nomina/departamentos/detalle.html', {'departamento': departamento})


@login_required
@permission_required('nomina.add_departamento', raise_exception=True)
def departamento_create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.creado_por = request.user
            departamento.save()
            messages.success(request, 'Departamento creado exitosamente.')
            return redirect('departamento_list')
    else:
        form = DepartamentoForm()
    return render(request, 'nomina/departamentos/formulario.html', {'form': form, 'accion': 'Crear'})


@login_required
@permission_required('nomina.change_departamento', raise_exception=True)
def departamento_update(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento actualizado exitosamente.')
            return redirect('departamento_detail', pk=departamento.pk)
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'nomina/departamentos/formulario.html', {'form': form, 'accion': 'Editar'})


@login_required
@permission_required('nomina.delete_departamento', raise_exception=True)
def departamento_delete(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        try:
            departamento.delete()
            messages.success(request, 'Departamento eliminado exitosamente.')
            return redirect('departamento_list')
        except ProtectedError:
            messages.error(request, 'No se puede eliminar el departamento porque tiene empleados asignados.')
            return redirect('departamento_detail', pk=departamento.pk)
    return render(request, 'nomina/departamentos/confirmar_eliminar.html', {'departamento': departamento})