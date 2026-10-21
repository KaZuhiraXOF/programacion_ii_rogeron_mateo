# tasks/urls.py
from django.urls import path
from . import views

app_name = "tasks"   # namespace de la app — ver nota más abajo

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("presentacion", views.presentacion, name="presentacion"),
    path("saludo/<str:nombre>", views.greeting, name="saludo"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>", 
        views.destination, name="destinatario"),
    path("area-triangulo/<int:base>/<int:altura>", 
        views.area_triangulo, name="area-triangulo"),
    path("my-first-template", views.my_first_template, 
        name="my-first-template"),
]   