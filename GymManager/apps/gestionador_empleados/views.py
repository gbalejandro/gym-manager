from django.shortcuts import render

def alta(request):
    return render(request, 'gestionador_empleados/altas.html')