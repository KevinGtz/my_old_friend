from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy #para regresar a otra url
from django.views.generic import ListView, DetailView #vistas para lista y detalle
from django.views.generic.edit import CreateView, UpdateView, DeleteView #vistas para modificar
from .models import Tienda #importamos el modelo


listaCampos = ['tienda', 'direccion', 'contacto'] #Lista de los campos para no repetir

#Lista de todas las tienda
class TiendaListView(ListView):
    model = Tienda #Con esto jala todo el modelo
    template_name = "index.html" #le decimos que template tiene que hacer el response

class TiendaDetail(DetailView):
	model = Tienda #con esto jala todo el modelo
	def get_context_data(self, **kwargs):
	    context = super(TiendaDetail, self).get_context_data(**kwargs)
	    return context #aqui regresa el resultado de la tienda solicitada

class TiendaCreate(CreateView):
	model = Tienda
	fields = listaCampos
	success_url = reverse_lazy('home') #con reverse_lazy le decimos que nos redirecciones cuando guarde el registro

class TiendaUpdate(UpdateView):
	model = Tienda
	fields = listaCampos
	success_url = reverse_lazy('home')

class TiendaDelete(DeleteView):
	model = Tienda
	success_url = reverse_lazy('home')