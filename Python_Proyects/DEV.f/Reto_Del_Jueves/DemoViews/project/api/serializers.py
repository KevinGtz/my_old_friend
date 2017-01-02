# -*- encoding:utf-8 -*-
from rest_framework import serializers #módulo que convierte nuestros modelos en json
from tienda.models import * #importamos nuestros modelos de tienda para que DRF sepá que objectos debe convertir a JSON

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio')

# class TiendaSerializer(serializers.ModelSerializer):
# 	productos = serializers.StringRelatedField(many=True)

# 	class Meta:
# 		model = Tienda
# 		fields = ('tienda', 'direccion', 'contacto', 'productos')

class TiendaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Tienda
        fields = ('tienda', 'direccion', 'contacto', 'productos')
