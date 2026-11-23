from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from nomina.models import Empleado
from nomina.forms import EmpleadoForm


def _puede_gestionar_empleado(user, empleado):
    es_admin = user.groups.filter(name='administradores').exists() or user.is_superuser
    return es_admin or empleado.creado_por == user

@login_required
def empleado_list(request):
    empleados = Empleado.objects.select_related('departamento', 'creado_por').all()
    return render(request, 'nomina/empleados/lista.html', {'empleados': empleados})

@login_required
def empleado_detail(request, pk):
    empleado = get_object_or_404(Empleado.objects.select_related('departamento', 'creado_por'), pk=pk)
    puede_editar = request.user.is_authenticated and _puede_gestionar_empleado(request.user, empleado)
    return render(request, 'nomina/empleados/detalle.html', {
        'empleado': empleado,
        'puede_editar': puede_editar,
    })


@login_required
@permission_required('nomina.add_empleado', raise_exception=True)
def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.creado_por = request.user
            empleado.save()
            messages.success(request, 'Empleado registrado exitosamente.')
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'nomina/empleados/formulario.html', {'form': form, 'accion': 'Registrar'})


@login_required
@permission_required('nomina.change_empleado', raise_exception=True)
def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if not _puede_gestionar_empleado(request.user, empleado):
        raise PermissionDenied
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos del empleado actualizados exitosamente.')
            return redirect('empleado_detail', pk=empleado.pk)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'nomina/empleados/formulario.html', {'form': form, 'accion': 'Editar'})


@login_required
@permission_required('nomina.delete_empleado', raise_exception=True)
def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if not _puede_gestionar_empleado(request.user, empleado):
        raise PermissionDenied
    if request.method == 'POST':
        try:
            empleado.delete()
            messages.success(request, 'Empleado eliminado exitosamente.')
            return redirect('empleado_list')
        except ProtectedError:
            messages.error(request, 'No se puede eliminar el empleado porque tiene roles de pago registrados.')
            return redirect('empleado_detail', pk=empleado.pk)
    return render(request, 'nomina/empleados/confirmar_eliminar.html', {'empleado': empleado})