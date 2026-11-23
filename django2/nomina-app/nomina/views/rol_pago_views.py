from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from nomina.models import RolPago
from nomina.forms import RolPagoForm


def _puede_gestionar_rol(user, rol):
    es_admin = user.groups.filter(name='administradores').exists() or user.is_superuser
    return es_admin or rol.creado_por == user


def _calcular_totales(rol):
    conceptos = rol.conceptos.all()
    ingresos_extra = sum(c.monto_fijo for c in conceptos if c.tipo == 'INGRESO')
    descuentos = sum(c.monto_fijo for c in conceptos if c.tipo == 'DESCUENTO')
    rol.total_ingresos = rol.empleado.salario_base + ingresos_extra
    rol.total_descuentos = descuentos
    rol.neto_a_pagar = rol.total_ingresos - rol.total_descuentos
    rol.save()

@login_required
def rol_list(request):
    roles = RolPago.objects.select_related('empleado', 'creado_por').prefetch_related('conceptos').all()
    return render(request, 'nomina/roles/lista.html', {'roles': roles})

@login_required
def rol_detail(request, pk):
    rol = get_object_or_404(
        RolPago.objects.select_related('empleado', 'empleado__departamento', 'creado_por').prefetch_related('conceptos'),
        pk=pk,
    )
    puede_editar = request.user.is_authenticated and _puede_gestionar_rol(request.user, rol)
    return render(request, 'nomina/roles/detalle.html', {
        'rol': rol,
        'puede_editar': puede_editar,
    })


@login_required
@permission_required('nomina.add_rolpago', raise_exception=True)
def rol_create(request):
    if request.method == 'POST':
        form = RolPagoForm(request.POST)
        if form.is_valid():
            rol = form.save(commit=False)
            rol.creado_por = request.user
            rol.save()
            form.save_m2m()
            _calcular_totales(rol)
            messages.success(request, 'Rol de pago generado exitosamente.')
            return redirect('rol_detail', pk=rol.pk)
    else:
        form = RolPagoForm()
    return render(request, 'nomina/roles/formulario.html', {'form': form, 'accion': 'Generar'})


@login_required
@permission_required('nomina.change_rolpago', raise_exception=True)
def rol_update(request, pk):
    rol = get_object_or_404(RolPago, pk=pk)
    if not _puede_gestionar_rol(request.user, rol):
        raise PermissionDenied
    if request.method == 'POST':
        form = RolPagoForm(request.POST, instance=rol)
        if form.is_valid():
            rol = form.save()
            _calcular_totales(rol)
            messages.success(request, 'Rol de pago actualizado exitosamente.')
            return redirect('rol_detail', pk=rol.pk)
    else:
        form = RolPagoForm(instance=rol)
    return render(request, 'nomina/roles/formulario.html', {'form': form, 'accion': 'Editar'})


@login_required
@permission_required('nomina.delete_rolpago', raise_exception=True)
def rol_delete(request, pk):
    rol = get_object_or_404(RolPago, pk=pk)
    if not _puede_gestionar_rol(request.user, rol):
        raise PermissionDenied
    if request.method == 'POST':
        rol.delete()
        messages.success(request, 'Rol de pago eliminado exitosamente.')
        return redirect('rol_list')
    return render(request, 'nomina/roles/confirmar_eliminar.html', {'rol': rol})