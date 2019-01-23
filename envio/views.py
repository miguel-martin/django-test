from django.shortcuts import render
from django.http import HttpResponse

from envio.models import Centro

# Create your views here.


def index(request):
    """ Renders a sample index page """
    return render(request, 'base.html', {'contents': 'My first app', 'titulo': 'Página ppal'})

def list_all_centros(request):
	""" Muestra informacion de todos los centros """
	centros = Centro.objects.all()
	return render(request, 'centros.html', {'centros': centros})
	
def list_centro(request, id):
	cid = int(id)
	avisos = ""
	try:
	    centros = [Centro.objects.get(cid=int(id))]
	except Centro.DoesNotExist:
		centros = []
		avisos = "El centro no existe"
	finally:
		return render(request, 'centros.html', locals())
