from django.contrib import admin

# Register your models here.
from .models import Project, NominaTrabajo


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(NominaTrabajo)
class NominaTrabajoAdmin(admin.ModelAdmin):
    list_display = ("nombre_trabajador", "anio_contrato", "sueldo_asignado", "created_at")
    search_fields = ("nombre_trabajador",)