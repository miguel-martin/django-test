from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from envio.models import Centro, Estudio, Plan
from django.views import generic



def index(request):
    """ Renders a sample index page """
    return render(request, 'base.html', {'contents': 'My first app', 'titulo': 'Página ppal'})

class CentroIndexView(generic.ListView):
	""" Muestra informacion de todos los centros """
	template_name = 'envios/centros_index.html'
	context_object_name = 'centros'

	def get_queryset(self):
		""" Genera el listado de todos los centros """
		return Centro.objects.order_by('nombre')
	
class CentroDetailView(generic.DetailView):
	""" Lista el centro id, si existe """ 
	model = Centro
	template_name = 'envios/centro_detail.html'

def edit_centro(request, id):
	""" Edita el centro id, si existe """
	return HttpResponseRedirect('/admin/envio/centro/{}/change'.format(id))

class EstudioIndexView(generic.ListView):
	""" Muestra informacion de todos los estudios """
	template_name = 'envios/estudios_index.html'
	context_object_name = 'estudios'

	def get_queryset(self):
		""" Genera el listado de todos estudios """
		return Estudio.objects.order_by('eid')	

class EstudioDetailView(generic.DetailView):
	""" Lista el esudio id, si existe """
	model = Estudio
	template_name = 'envios/estudios_detail.html'

def edit_estudio(request, id):
	""" Edita el estudio id, si existe """
	return HttpResponseRedirect('/admin/envio/estudio/{}/change'.format(id))

class PlanIndexView(generic.ListView):
	""" Muestra informacion de todos los planes """
	template_name = 'envios/plan_index.html'
	context_object_name = 'planes'

	def get_queryset(self):
		""" Genera el listado de todos los planes"""
		return Plan.objects.order_by('pid')

class PlanDetailView(generic.DetailView):
	""" Lista el plan id, si existe """ 
	model = Plan
	template_name = 'envios/plan_detail.html'

def edit_plan(request, id):
	""" Edita el plan id, si existe """
	return HttpResponseRedirect('/admin/envio/plan/{}/change/'.format(id))

