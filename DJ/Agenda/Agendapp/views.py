from django.shortcuts import render
from Agendapp.models import Jugador

# Create your views here.
def landing_page(request):
	# lookups
	jugadores = Jugador.objects.filter(nombre__iexact='Oscar', edad__gt=16)


	jugadores = jugadores.order_by('nombre')
	for jugador in jugadores:
		print jugador.nombr
e	return render(request, 'home.html', { 'jugadores': jugadores })