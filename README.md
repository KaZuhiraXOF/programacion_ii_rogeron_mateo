# Programación II

# Autor: Mateo Rogeron

Repositorio centralizado para el almacenamiento de código, prácticas y proyectos correspondientes a la materia. El contenido cubre el desarrollo de software backend y empresarial mediante tres pilares tecnológicos:

---

## 🐍 Python
Base lógica del repositorio. Se enfoca en:
* Programación Orientada a Objetos (POO): clases, herencia, polimorfismo y encapsulamiento.
* Manejo de excepciones, lectura/escritura de archivos y estructuras de datos.
* Escritura de código limpio y modular bajo las convenciones de estilo de Python (PEP 8).

## 🌐 Django
Framework web de alto nivel enfocado en el desarrollo ágil y seguro:
* Arquitectura basada en el patrón MVT (Modelo - Vista - Template).
* Manejo de base de datos a través del ORM de Django (modelos, migraciones y consultas).
* Creación de vistas (basadas en funciones y en clases), formularios, autenticación y manejo de sesiones.
* Configuración de rutas URL y renderizado de plantillas dinámicas.

## 🏢 Odoo ERP
Plataforma de gestión empresarial orientada al desarrollo modular:
* Creación y arquitectura de módulos personalizados (Addons).
* Modelado de datos en PostgreSQL mediante el ORM propio de Odoo (`models.Model`).
* Manejo de campos relacionales (`Many2one`, `One2many`, `Many2many`) y lógica de negocio (`@api.depends`, `@api.onchange`, `@api.constrains`).
* Construcción de interfaces de usuario (vistas de lista, formulario y búsqueda) y menús mediante archivos XML.

---

### Entorno de Trabajo
* **Lenguaje:** Python 3.x
* **Bases de datos:** SQLite (desarrollo local / Django) y PostgreSQL (Odoo / Django producción).
* **Gestión de dependencias:** Aislamiento de paquetes mediante entornos virtuales (`venv`) específicos para cada componente.