from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from envio.models import Centro, Estudio, Plan, Persona, Matricula, Entrega
from django.views import generic
from django.urls import reverse
from .forms import EntregaForm



def index(request):
    """ Renders a sample index page """
    return render(request, 'envio/base.html', {'contents': 'Use la barra superior para navegar', 'titlepag': 'Gestión de Trabajos'})

class CentroIndexView(generic.ListView):
	""" Muestra informacion de todos los centros """
	template_name = 'envio/centros_index.html'
	context_object_name = 'centros'

	def get_queryset(self):
		""" Genera el listado de todos los centros """
		return Centro.objects.order_by('nombre')
	
class CentroDetailView(generic.DetailView):
	""" Lista el centro id, si existe """ 
	model = Centro
	template_name = 'envio/centro_detail.html'

def edit_centro(request, id):
	""" Edita el centro id, si existe """
	return HttpResponseRedirect('/admin/envio/centro/{}/change'.format(id))

class EstudioIndexView(generic.ListView):
	""" Muestra informacion de todos los estudios """
	template_name = 'envio/estudios_index.html'
	context_object_name = 'estudios'

	def get_queryset(self):
		""" Genera el listado de todos estudios """
		return Estudio.objects.order_by('eid')	

class EstudioDetailView(generic.DetailView):
	""" Lista el esudio id, si existe """
	model = Estudio
	template_name = 'envio/estudio_detail.html'

def edit_estudio(request, id):
	""" Edita el estudio id, si existe """
	return HttpResponseRedirect('/admin/envio/estudio/{}/change'.format(id))

class PlanIndexView(generic.ListView):
	""" Muestra informacion de todos los planes """
	template_name = 'envio/plan_index.html'
	context_object_name = 'planes'

	def get_queryset(self):
		""" Genera el listado de todos los planes"""
		return Plan.objects.order_by('pid')

class PlanDetailView(generic.DetailView):
	""" Lista el plan id, si existe """ 
	model = Plan
	template_name = 'envio/plan_detail.html'

def edit_plan(request, id):
	""" Edita el plan id, si existe """
	return HttpResponseRedirect('/admin/envio/plan/{}/change/'.format(id))

class PersonaIndexView(generic.ListView):
	""" Muestra informacion de todas las personas """
	template_name = 'envio/persona_index.html'
	context_object_name = 'personas'

	def get_queryset(self):
		""" Genera el listado de todas las personas por orden de sus apellidos """
		return Persona.objects.order_by('apellidos')

class PersonaDetailView(generic.DetailView):
	""" Lista la persona, si existe """ 
	model = Persona
	template_name = 'envio/persona_detail.html'

class MatriculaIndexView(generic.ListView):
	""" Muestra informacion de todas las matriculas """
	template_name = 'envio/matricula_index.html'
	context_object_name = 'matriculas'

	def get_queryset(self):
		""" Genera el listado de todas las matriculas por orden de sus apellidos """
		return Matricula.objects.all()

class MatriculaDetailView(generic.DetailView):
	""" Lista la matricula, si existe """ 
	model = Matricula
	template_name = 'envio/matricula_detail.html'

class EntregaIndexView(generic.ListView):
	""" Muestra informacion de todas las matriculas """
	template_name = 'envio/entrega_index.html'
	context_object_name = 'entregas'

	def get_queryset(self):
		""" Genera el listado de todas las matriculas por orden de sus apellidos """
		return Entrega.objects.all()

class EntregaDetailView(generic.DetailView):
	""" Lista la entrega, si existe """ 
	model = Entrega
	template_name = 'envio/entrega_detail.html'


def edit_or_create_Entrega(request, nip):
	""" Muestra el form para realizar entregas """
	if request.method == "POST":
		# create form instance and populate it with data from the request
		form = EntregaForm(request.POST)
		if form.is_valid():
			# ToDo procesar
			# ToDo guardar
			nueva_entrega = form.save()
			# redirigir
			return HttpResponseRedirect(reverse('list_entrega', kwargs={'tid':nueva_entrega.tid}))
	else:
		# if a GET (or any other method) we'll create a blank form
		# we'll limit the Matricula choices to the ones that correspond to that nip
		form = EntregaForm()
		matriculas = get_list_or_404(Matricula, persona__nip=nip)
		matriculas_filtered_choices = []
		for matricula in matriculas:
			matriculas_filtered_choices.append([matricula.pk, matricula.get_nombre_estudio()])
		form.fields['matricula'].choices = matriculas_filtered_choices

	return render(request, 'envio/entrega_form.html', {'form': form})
	





