from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
	d = Destino.mexico.all()
	print(d)
	return render(request, 'index.html', {'destinos':d})
