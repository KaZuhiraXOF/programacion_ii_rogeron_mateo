# Register your models here.
from django.contrib import admin
from nomina.models import Departamento, Empleado, ConceptoSalarial, RolPago


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'ubicacion', 'creado_por')
    list_filter = ('ubicacion',)
    search_fields = ('codigo', 'nombre', 'ubicacion')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'apellidos', 'nombres', 'departamento', 'salario_base', 'estado')
    list_filter = ('estado', 'departamento', 'fecha_ingreso')
    search_fields = ('cedula', 'nombres', 'apellidos', 'correo')


@admin.register(ConceptoSalarial)
class ConceptoSalarialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'monto_fijo', 'es_recurrente')
    list_filter = ('tipo', 'es_recurrente')
    search_fields = ('nombre',)


@admin.register(RolPago)
class RolPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'empleado', 'periodo_inicio', 'periodo_fin', 'neto_a_pagar', 'estado_pago', 'creado_por')
    list_filter = ('estado_pago', 'periodo_fin', 'empleado__departamento')
    search_fields = ('empleado__cedula', 'empleado__apellidos', 'empleado__nombres')
    filter_horizontal = ('conceptos',)