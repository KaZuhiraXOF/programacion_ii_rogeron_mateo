from django.urls import path
from nomina.views import (
    concepto_list,
    concepto_detail,
    concepto_create,
    concepto_update,
    concepto_delete,
)

urlpatterns = [
    path('', concepto_list, name='concepto_list'),
    path('<int:pk>/', concepto_detail, name='concepto_detail'),
    path('crear/', concepto_create, name='concepto_create'),
    path('<int:pk>/editar/', concepto_update, name='concepto_update'),
    path('<int:pk>/eliminar/', concepto_delete, name='concepto_delete'),
]