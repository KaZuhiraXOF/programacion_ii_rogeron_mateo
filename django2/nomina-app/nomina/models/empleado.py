from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from nomina.models.departamento import Departamento


class Empleado(models.Model):
    class EstadoEmpleado(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        INACTIVO = 'INACTIVO', 'Inactivo'
        VACACIONES = 'VACACIONES', 'En vacaciones'

    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cédula')
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    correo = models.EmailField(unique=True, verbose_name='Correo electrónico')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    salario_base = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Salario base',
    )
    estado = models.CharField(
        max_length=15,
        choices=EstadoEmpleado.choices,
        default=EstadoEmpleado.ACTIVO,
        verbose_name='Estado',
    )
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.PROTECT,
        related_name='empleados',
        verbose_name='Departamento',
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='empleados_creados',
        verbose_name='Creado por',
    )

    class Meta:
        ordering = ['apellidos', 'nombres']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'{self.apellidos} {self.nombres} ({self.cedula})'

    def get_absolute_url(self):
        return reverse('empleado_detail', kwargs={'pk': self.pk})