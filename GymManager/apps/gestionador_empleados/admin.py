from django.contrib import admin

from apps.gestionador_empleados.models import Dirección, Empleado
# Register your models here.

admin.site.register(Dirección)
admin.site.register(Empleado)