from django.db import models
from django.urls import reverse


class ConceptoSalarial(models.Model):
    class TipoConcepto(models.TextChoices):
        INGRESO = 'INGRESO', 'Ingreso / Bono'
        DESCUENTO = 'DESCUENTO', 'Descuento / Deducción'

    nombre = models.CharField(max_length=100, unique=True, verbose_name='Concepto')
    tipo = models.CharField(
        max_length=15,
        choices=TipoConcepto.choices,
        default=TipoConcepto.INGRESO,
        verbose_name='Tipo',
    )
    monto_fijo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Monto fijo',
    )
    es_recurrente = models.BooleanField(default=True, verbose_name='Es recurrente')

    class Meta:
        ordering = ['tipo', 'nombre']
        verbose_name = 'Concepto salarial'
        verbose_name_plural = 'Conceptos salariales'

    def __str__(self):
        return f'{self.nombre} ({self.get_tipo_display()} - ${self.monto_fijo})'

    def get_absolute_url(self):
        return reverse('concepto_detail', kwargs={'pk': self.pk})