from django.urls import path
from nomina.views import (
    empleado_list,
    empleado_detail,
    empleado_create,
    empleado_update,
    empleado_delete,
)

urlpatterns = [
    path('', empleado_list, name='empleado_list'),
    path('<int:pk>/', empleado_detail, name='empleado_detail'),
    path('crear/', empleado_create, name='empleado_create'),
    path('<int:pk>/editar/', empleado_update, name='empleado_update'),
    path('<int:pk>/eliminar/', empleado_delete, name='empleado_delete'),
]