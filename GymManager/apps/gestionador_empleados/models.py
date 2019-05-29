from django.db import models

# Create your models here.

class Dirección(models.Model):
	"""Contiene toda la información relevante a la dirección de una persona"""
	calle = models.CharField(max_length=50)
	numero_exterior = models.CharField(max_length=50)
	numero_interior = models.CharField(max_length=50)
	manzana = models.CharField(max_length=50)
	lote = models.CharField(max_length=50)
	código_postal = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)
	estado = models.CharField(max_length=50) 

class Persona(models.Model):
	"""Persona hereda a Empleado y Cliente"""
	nombre = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	teléfono = models.IntegerField()
	password = models.CharField(max_length=50) #agregar passwordinput en form
	fecha_nacimiento = models.DateField()
	dirección = models.ForeignKey(
		Dirección, 
		on_delete=models.CASCADE,)

	class Meta:
		abstract = True

class Empleado(Persona):
	"""Empleado representa a todos los personajes que existen
	en la jerarquía de la empresa."""
	puesto = models.CharField(max_length=50)


		