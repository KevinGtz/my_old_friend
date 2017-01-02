# -*- encoding: utf-8 -*-
from rest_framework.views import APIView #Con esto le indicamos al View que va a heredar el comportamiente de APIView de DRF
from rest_framework.response import Response #Este módulo de DRF hace las negociaciones HTTP que permite responder con el "content-type" solicitado por el cliente
from rest_framework import generics #Clase Base Views Generics
from rest_framework import status #Est módulo se encarga de especificar en la respuesta el código de estatus de la misma, ejemplo 200 si es exitosa o 400 si hay error
from rest_framework import filters #Módulo para filtrar los datos vía url
from django.http import Http404 #este módulo se encarga de manejar el comportamiento de la aplicación en el momento que no se encuente una url
from .serializers import * #importamos los serializer previamente creados para decirle al view cual debe de utilizar para regresar o recibir el JSON

#Class Based Views Demos
#================================================================================#
# class TiendaView(APIView):
# 	def get(self, request, format=None):
# 		tiendas = Tienda.objects.all()
# 		serializer = TiendaSerializer(tiendas, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = TiendaSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TiendaDetailView(APIView):

# 	def get_object(self, pk):
# 		try:
# 			return Tienda.objects.get(pk=pk)
# 		except Tienda.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		tienda = self.get_object(pk)
# 		serializer = TiendaSerializer(tienda, many=False)
# 		return Response(serializer.data, status.HTTP_200_OK)

# 	def put(self, request, pk, format=None):
# 		tienda = self.get_object(pk)
# 		serializer = TiendaSerializer(tienda, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		tienda = self.get_object(pk)
# 		tienda.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
#================================================================================#

#Generics Views
#================================================================================#
# class TiendaView(generics.ListCreateAPIView):
# 	queryset = Tienda.objects.all()
# 	serializer_class = TiendaSerializer

class TiendaView(generics.ListCreateAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('contacto',)



class TiendaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class ProductoCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


    #================================================================================#