from django.urls import path
from nomina.views import (
    departamento_list,
    departamento_detail,
    departamento_create,
    departamento_update,
    departamento_delete,
)

urlpatterns = [
    path('', departamento_list, name='departamento_list'),
    path('<int:pk>/', departamento_detail, name='departamento_detail'),
    path('crear/', departamento_create, name='departamento_create'),
    path('<int:pk>/editar/', departamento_update, name='departamento_update'),
    path('<int:pk>/eliminar/', departamento_delete, name='departamento_delete'),
]