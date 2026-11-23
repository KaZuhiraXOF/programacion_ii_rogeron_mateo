from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from nomina.models import ConceptoSalarial
from nomina.forms import ConceptoSalarialForm


def concepto_list(request):
    conceptos = ConceptoSalarial.objects.all()
    return render(request, 'nomina/conceptos/lista.html', {'conceptos': conceptos})


def concepto_detail(request, pk):
    concepto = get_object_or_404(ConceptoSalarial, pk=pk)
    return render(request, 'nomina/conceptos/detalle.html', {'concepto': concepto})


@login_required
@permission_required('nomina.add_conceptosalarial', raise_exception=True)
def concepto_create(request):
    if request.method == 'POST':
        form = ConceptoSalarialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concepto salarial creado exitosamente.')
            return redirect('concepto_list')
    else:
        form = ConceptoSalarialForm()
    return render(request, 'nomina/conceptos/formulario.html', {'form': form, 'accion': 'Crear'})


@login_required
@permission_required('nomina.change_conceptosalarial', raise_exception=True)
def concepto_update(request, pk):
    concepto = get_object_or_404(ConceptoSalarial, pk=pk)
    if request.method == 'POST':
        form = ConceptoSalarialForm(request.POST, instance=concepto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concepto salarial actualizado exitosamente.')
            return redirect('concepto_detail', pk=concepto.pk)
    else:
        form = ConceptoSalarialForm(instance=concepto)
    return render(request, 'nomina/conceptos/formulario.html', {'form': form, 'accion': 'Editar'})


@login_required
@permission_required('nomina.delete_conceptosalarial', raise_exception=True)
def concepto_delete(request, pk):
    concepto = get_object_or_404(ConceptoSalarial, pk=pk)
    if request.method == 'POST':
        concepto.delete()
        messages.success(request, 'Concepto salarial eliminado exitosamente.')
        return redirect('concepto_list')
    return render(request, 'nomina/conceptos/confirmar_eliminar.html', {'concepto': concepto})