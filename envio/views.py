from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from envio.models import Centro, Estudio, Plan

# Create your views here.


def index(request):
    """ Renders a sample index page """
    return render(request, 'base.html', {'contents': 'My first app', 'titulo': 'Página ppal'})

def list_all_centros(request):
	""" Muestra informacion de todos los centros """
	centros = Centro.objects.all()
	return render(request, 'envios/centros.html', {'centros': centros})
	
def list_centro(request, id):
	""" Lista el centro id, si existe """ 
	cid = int(id)
	centro = get_object_or_404(Centro, cid=cid)	
	return render(request, 'envios/centros.html', {'cid': cid, 'centros': [centro]})

def edit_centro(request, id):
	""" Edita el centro id, si existe """
	return HttpResponseRedirect('/admin/envio/centro/{}/change'.format(id))

#def delete_centro(request, id):
#	""" Borra el centro id, si existe """
#	pass 	

def list_all_estudios(request):
	""" Muestra informacion de todos los estudios """
	estudios = Estudio.objects.all()
	return render(request, 'envios/estudios.html', {'estudios': estudios})

def list_estudio(request, id):
	""" Lista el estudio id, si existe """ 
	eid = int(id)
	estudio = get_object_or_404(Estudio, eid=eid)
	return render(request, 'envios/estudios.html', {'eid': eid, 'estudios':[estudio]})

def edit_estudio(request, id):
	""" Edita el estudio id, si existe """
	return HttpResponseRedirect('/admin/envio/estudio/{}/change'.format(id))

#def delete_estudio(request, id):
#	""" Borra el estudio id, si existe """
#	pass

def list_all_planes(request):
	""" Muestra informacion de todos los planes """
	planes = Plan.objects.all()
	return render(request, 'envios/planes.html', {'planes': planes})

def list_plan(request, id):
	""" Lista el plan id, si existe """ 
	pid = int(id)
	plan = get_object_or_404(Plan, pid=pid)
	return render(request, 'envios/planes.html', {'pid': pid, 'planes': [plan]})

def edit_plan(request, id):
	""" Edita el plan id, si existe """
	return HttpResponseRedirect('/admin/envio/plan/{}/change/'.format(id))