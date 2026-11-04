
from django.urls import path
from catalogo.views.categoria_view import (categoria_list, 
                                categoria_create,)

urlpatterns = [
    path('', 
        categoria_list, 
        name='categoria_list'),
    path('crear/', 
        categoria_create, 
        name='categoria_create'),
]
