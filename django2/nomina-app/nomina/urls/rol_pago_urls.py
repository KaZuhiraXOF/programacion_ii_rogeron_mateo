from django.urls import path
from nomina.views import (
    rol_list,
    rol_detail,
    rol_create,
    rol_update,
    rol_delete,
)

urlpatterns = [
    path('', rol_list, name='rol_list'),
    path('<int:pk>/', rol_detail, name='rol_detail'),
    path('crear/', rol_create, name='rol_create'),
    path('<int:pk>/editar/', rol_update, name='rol_update'),
    path('<int:pk>/eliminar/', rol_delete, name='rol_delete'),
]