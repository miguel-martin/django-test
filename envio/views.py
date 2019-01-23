from django.shortcuts import render
from django.http import HttpResponse

from envio.models import Centro, Estudio, Plan

# Create your views here.


def index(request):
    """ Renders a sample index page """
    return render(request, 'base.html', {'contents': 'My first app', 'titulo': 'Página ppal'})

def list_all_centros(request):
	""" Muestra informacion de todos los centros """
	centros = Centro.objects.all()
	return render(request, 'centros.html', {'centros': centros})
	
def list_centro(request, id):
	""" Lista el centro id, si existe """ 
	cid = int(id)
	try:
	    centros = [Centro.objects.get(cid=int(id))]
	except Centro.DoesNotExist:
		centros = []
		avisos = "El centro no {} existe".format(cid)
	finally:
		return render(request, 'centros.html', locals())

def edit_centro(request, id):
	""" Edita el centro id, si existe """
	pass

def delete_centro(request, id):
	""" Borra el centro id, si existe """
	pass 	

def list_all_estudios(request):
	""" Muestra informacion de todos los estudios """
	estudios = Estudio.objects.all()
	return render(request, 'estudios.html', {'estudios': estudios})

def list_estudio(request, id):
	""" Lista el estudio id, si existe """ 
	eid = int(id)
	try:
	    estudios = [Estudio.objects.get(eid=int(id))]
	except Estudio.DoesNotExist:
		estudios = []
		avisos = "El estudio {} no existe".format(eid)
	finally:
		return render(request, 'estudios.html', locals())

def edit_estudio(request, id):
	""" Edita el estudio id, si existe """
	pass

def delete_estudio(request, id):
	""" Borra el estudio id, si existe """
	pass

def list_all_planes(request):
	""" Muestra informacion de todos los planes """
	planes = Plan.objects.all()
	return render(request, 'planes.html', {'planes': planes})

def list_plan(request, id):
	""" Lista el plan id, si existe """ 
	pid = int(id)
	try:
	    planes = [Plan.objects.get(pid=int(id))]
	except Plan.DoesNotExist:
		planes = []
		avisos = "El plan {} no existe".format(eid)
	finally:
		return render(request, 'planes.html', locals())