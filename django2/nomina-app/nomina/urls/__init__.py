from django.urls import path, include

urlpatterns = [
    path('', include('nomina.urls.rol_pago_urls')),
    path('departamentos/', include('nomina.urls.departamento_urls')),
    path('empleados/', include('nomina.urls.empleado_urls')),
    path('conceptos/', include('nomina.urls.concepto_urls')),
    path('cuenta/', include('nomina.urls.auth_urls')),
]