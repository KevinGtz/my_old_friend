from __future__ import unicode_literals
from django.db import models

# Crea modelo tienda
class Tienda(models.Model):

    class Meta:
        verbose_name = "Tienda" #nombre para el objeto en singular
        verbose_name_plural = "Tiendas" #nombre para el objeto en plural


    #Attributes
    tienda = models.CharField(max_length=50, blank=False, unique=True) #campo tipo string, unico y obligatorio
    direccion = models.CharField(max_length=150, blank=False)
    contacto = models.CharField(max_length=60, blank=False)


    def __str__(self):
        return (self.tienda) #Regresamos el nombre de la tienda para el admin


class Producto(models.Model):

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    #Relations
    tienda = models.ForeignKey(Tienda, related_name='productos')

    #Attributes
    nombre = models.CharField(max_length=50, blank=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return(self.nombre)
