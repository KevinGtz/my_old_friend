from django.contrib import admin
from .models import Tienda, Producto
# Register your models here.
admin.site.register(Tienda) #Agregamos tienda al admin
admin.site.register(Producto)