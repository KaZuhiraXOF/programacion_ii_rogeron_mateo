from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from nomina.models.empleado import Empleado
from nomina.models.concepto_salarial import ConceptoSalarial


class RolPago(models.Model):
    class EstadoPago(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        APROBADO = 'APROBADO', 'Aprobado'
        PAGADO = 'PAGADO', 'Pagado'

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.PROTECT,
        related_name='roles_pago',
        verbose_name='Empleado',
    )
    conceptos = models.ManyToManyField(
        ConceptoSalarial,
        related_name='roles_pago',
        blank=True,
        verbose_name='Conceptos aplicados',
    )
    periodo_inicio = models.DateField(verbose_name='Inicio de período')
    periodo_fin = models.DateField(verbose_name='Fin de período')
    fecha_emision = models.DateField(auto_now_add=True, verbose_name='Fecha de emisión')
    total_ingresos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Total ingresos',
    )
    total_descuentos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Total descuentos',
    )
    neto_a_pagar = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Neto a pagar',
    )
    estado_pago = models.CharField(
        max_length=15,
        choices=EstadoPago.choices,
        default=EstadoPago.BORRADOR,
        verbose_name='Estado del pago',
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='roles_creados',
        verbose_name='Creado por',
    )

    class Meta:
        ordering = ['-periodo_fin', 'empleado']
        verbose_name = 'Rol de pago'
        verbose_name_plural = 'Roles de pago'

    def __str__(self):
        return f'Rol #{self.pk} - {self.empleado.apellidos} ({self.periodo_inicio} al {self.periodo_fin})'

    def get_absolute_url(self):
        return reverse('rol_detail', kwargs={'pk': self.pk})