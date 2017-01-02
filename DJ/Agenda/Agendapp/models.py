from django.db import models

# Create your models here.

class Jugador(models.Model):
	nombre = models.CharField(max_length=30)
	edad = models.IntegerField()
	ubicacion = models.CharField(max_length=50)
	avatar = models.ImageField()

class Cancha(models.Model):
	nombre = models.CharField(max_length=30)
	telefono = models.CharField(max_length=14)
	ubicacion = models.CharField(max_length=50)
	raiting = models.PositiveIntegerField()
	imagenes = models.ImageField()
	precio = models.PositiveIntegerField()

class Reta(models.Model):
	horario = models.DateTimeField()
	precio = models.PositiveIntegerField()
	tipo_reta = models.CharField(max_length=50)

class Equipo(models.Model):
	nombre = models.CharField(max_length=30)
	num_jugadores = models.PositiveIntegerField()



			
