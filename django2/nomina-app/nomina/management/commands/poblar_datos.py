from datetime import date
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from nomina.models import Departamento, Empleado, ConceptoSalarial, RolPago


class Command(BaseCommand):
    help = 'Crea grupos, permisos, usuarios de prueba y al menos 5 registros por tabla.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Configurando grupos y permisos...')

        admin_group, _ = Group.objects.get_or_create(name='administradores')
        consultor_group, _ = Group.objects.get_or_create(name='consultores')

        # Asignar todos los permisos de los modelos de nomina al grupo administradores
        modelos = [Departamento, Empleado, ConceptoSalarial, RolPago]
        permisos_admin = []
        for modelo in modelos:
            ct = ContentType.objects.get_for_model(modelo)
            permisos_admin.extend(Permission.objects.filter(content_type=ct))
        admin_group.permissions.set(permisos_admin)

        # Asignar permisos limitados al grupo consultores:
        # Pueden ver todo, y crear/editar/eliminar sus propios Roles de Pago y Empleados
        permisos_consultor = []
        for modelo in modelos:
            ct = ContentType.objects.get_for_model(modelo)
            permisos_consultor.extend(
                Permission.objects.filter(content_type=ct, codename__startswith='view_')
            )
        for modelo in [RolPago, Empleado]:
            ct = ContentType.objects.get_for_model(modelo)
            permisos_consultor.extend(
                Permission.objects.filter(
                    content_type=ct,
                    codename__in=[
                        f'add_{modelo._meta.model_name}',
                        f'change_{modelo._meta.model_name}',
                        f'delete_{modelo._meta.model_name}',
                    ],
                )
            )
        consultor_group.permissions.set(permisos_consultor)

        self.stdout.write('Creando usuarios de prueba...')
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nomina.local', 'Admin1234!')

        user_admin, created = User.objects.get_or_create(
            username='jefe_nomina',
            defaults={'email': 'jefe@nomina.local', 'first_name': 'Carlos', 'last_name': 'Mendoza'},
        )
        if created:
            user_admin.set_password('Nomina1234!')
            user_admin.save()
        user_admin.groups.add(admin_group)

        user_consultor, created = User.objects.get_or_create(
            username='asistente_rrhh',
            defaults={'email': 'asistente@nomina.local', 'first_name': 'Laura', 'last_name': 'Vega'},
        )
        if created:
            user_consultor.set_password('Consulta1234!')
            user_consultor.save()
        user_consultor.groups.add(consultor_group)

        self.stdout.write('Poblando Departamentos (5 registros)...')
        deptos_data = [
            ('DEP-TI', 'Tecnología e Informática', 'Piso 3 - Ala Norte'),
            ('DEP-RH', 'Talento Humano', 'Piso 1 - Recepción'),
            ('DEP-FN', 'Contabilidad y Finanzas', 'Piso 2 - Ala Sur'),
            ('DEP-OP', 'Operaciones y Logística', 'Planta Baja - Bodega'),
            ('DEP-MK', 'Marketing y Ventas', 'Piso 2 - Ala Norte'),
        ]
        deptos = []
        for codigo, nombre, ubicacion in deptos_data:
            depto, _ = Departamento.objects.get_or_create(
                codigo=codigo,
                defaults={'nombre': nombre, 'ubicacion': ubicacion, 'creado_por': user_admin},
            )
            deptos.append(depto)

        self.stdout.write('Poblando Empleados (5 registros)...')
        empleados_data = [
            ('1710034065', 'Mateo', 'Rogeron', 'mateo.rogeron@empresa.ec', date(2023, 3, 15), Decimal('1450.00'), 'ACTIVO', deptos[0], user_admin),
            ('1723456781', 'Sofía', 'Paredes', 'sofia.paredes@empresa.ec', date(2022, 6, 1), Decimal('1300.00'), 'ACTIVO', deptos[1], user_admin),
            ('0912345678', 'Andrés', 'Villavicencio', 'andres.villa@empresa.ec', date(2021, 11, 10), Decimal('1600.00'), 'VACACIONES', deptos[2], user_consultor),
            ('1709876543', 'Valeria', 'Cárdenas', 'valeria.cardenas@empresa.ec', date(2024, 1, 20), Decimal('980.00'), 'ACTIVO', deptos[3], user_consultor),
            ('1804567890', 'Diego', 'Salazar', 'diego.salazar@empresa.ec', date(2023, 8, 5), Decimal('1150.00'), 'INACTIVO', deptos[4], user_admin),
        ]
        empleados = []
        for cedula, nombres, apellidos, correo, ingreso, salario, estado, depto, creador in empleados_data:
            emp, _ = Empleado.objects.get_or_create(
                cedula=cedula,
                defaults={
                    'nombres': nombres,
                    'apellidos': apellidos,
                    'correo': correo,
                    'fecha_ingreso': ingreso,
                    'salario_base': salario,
                    'estado': estado,
                    'departamento': depto,
                    'creado_por': creador,
                },
            )
            empleados.append(emp)

        self.stdout.write('Poblando Conceptos Salariales (5 registros)...')
        conceptos_data = [
            ('Bono de Alimentación', 'INGRESO', Decimal('80.00'), True),
            ('Horas Suplementarias 50%', 'INGRESO', Decimal('120.50'), False),
            ('Bono por Cumplimiento', 'INGRESO', Decimal('150.00'), False),
            ('Aporte Personal IESS (9.45%)', 'DESCUENTO', Decimal('115.00'), True),
            ('Anticipo de Quincena', 'DESCUENTO', Decimal('200.00'), False),
        ]
        conceptos = []
        for nombre, tipo, monto, recurrente in conceptos_data:
            conc, _ = ConceptoSalarial.objects.get_or_create(
                nombre=nombre,
                defaults={'tipo': tipo, 'monto_fijo': monto, 'es_recurrente': recurrente},
            )
            conceptos.append(conc)

        self.stdout.write('Poblando Roles de Pago (5 registros)...')
        if RolPago.objects.count() < 5:
            roles_config = [
                (empleados[0], [conceptos[0], conceptos[1], conceptos[3]], 'PAGADO', user_admin),
                (empleados[1], [conceptos[0], conceptos[3]], 'PAGADO', user_admin),
                (empleados[2], [conceptos[0], conceptos[2], conceptos[3], conceptos[4]], 'APROBADO', user_consultor),
                (empleados[3], [conceptos[0], conceptos[3]], 'BORRADOR', user_consultor),
                (empleados[4], [conceptos[3], conceptos[4]], 'BORRADOR', user_admin),
            ]
            for emp, lista_conc, estado_p, creador in roles_config:
                ingresos = emp.salario_base + sum(c.monto_fijo for c in lista_conc if c.tipo == 'INGRESO')
                descuentos = sum(c.monto_fijo for c in lista_conc if c.tipo == 'DESCUENTO')
                rol = RolPago.objects.create(
                    empleado=emp,
                    periodo_inicio=date(2026, 10, 1),
                    periodo_fin=date(2026, 10, 31),
                    total_ingresos=ingresos,
                    total_descuentos=descuentos,
                    neto_a_pagar=ingresos - descuentos,
                    estado_pago=estado_p,
                    creado_por=creador,
                )
                rol.conceptos.set(lista_conc)

        self.stdout.write(self.style.SUCCESS('¡Datos, grupos y usuarios creados exitosamente!'))