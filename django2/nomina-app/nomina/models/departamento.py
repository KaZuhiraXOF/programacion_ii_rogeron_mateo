from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    codigo = models.CharField(max_length=15, unique=True, verbose_name='Código')
    ubicacion = models.CharField(max_length=120, verbose_name='Ubicación')
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departamentos_creados',
        verbose_name='Creado por',
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f'{self.codigo} ({self.nombre})'

    def get_absolute_url(self):
        return reverse('departamento_detail', kwargs={'pk': self.pk})