from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>TaskFlow</h1>
                <p>Bienvenido al sistema</p>
            </body>
        </html>
    """)

def register(request):
    """Registros de usuarios"""
    return HttpResponse("Registros de Usuarios en línea")

def presentacion(request):
    """Presentacion del programador"""
    return HttpResponse("Si ves esta línea de código, es que hice algo y funcionó - mateo rogeron")

def greeting(request, nombre):
    """"Registro de usuarios"""
    return HttpResponse(
        f"Hola, {nombre}. Bienvenido a TaskFlow"
    )

def destination(request, titulo, nombre, cargo):
    """"Registro de usuarios"""
    return HttpResponse(
        f"Bienvenido,{titulo} {nombre}, su cargo es {cargo}"
    )

def area_triangulo(request, base, altura):
    """Calcula el área de un triángulo"""
    return HttpResponse(f"El área del triángulo es: {(base * altura) / 2}")

def my_first_template(request):
    contexto = {
        "titulo": "TaskFlow",
        "mensaje": "Organiza tus proyectos y tareas en un solo lugar",
    }
    return render(request, "tasks/my-first-template.html", contexto)