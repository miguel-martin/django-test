from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from envio.models import Centro, Estudio, Plan, Persona, Matricula, Entrega
from django.views import generic
from django.urls import reverse
from .forms import EntregaForm, UserForm, EntregasCentroForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from private_storage.views import PrivateStorageDetailView


def index(request):
    """ Renders a sample index page """
    return render(request, 'envio/index.html', {'contents': 'Use la barra superior para navegar', 'titlepag': 'Gestión de Trabajos'})

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
	#ordering = ['-fecha']
	ordering = ['fecha']

	def get_queryset(self):
		""" Genera el listado de todas las matriculas por orden de sus apellidos """
		return Entrega.objects.filter(matricula__persona__user=self.request.user)

class EntregaDetailView(generic.DetailView):
	""" Lista la entrega, si existe """ 
	model = Entrega
	template_name = 'envio/entrega_detail.html'

class AnexosDownloadView(PrivateStorageDetailView):
	model = Entrega
	model_file_field = 'anexos'

    #FIXME
    #def get_queryset(self):
    #    # Make sure only certain objects can be accessed.
    #    # Filter only the files that belong to that entrega and belong to self.request.user
    #    return super().get_queryset().filter(...) 

	def can_access_file(self, private_file):
		is_loggedin = (not self.request.user.is_anonymous) and self.request.user.is_authenticated
		is_tribunal = False #ToDo
		is_secretaria = False #ToDo
		is_owner = self.object.matricula.persona.user.pk == private_file.request.user.pk
		return is_loggedin and (is_owner or is_tribunal or is_secretaria)


class MemoriaDownloadView(PrivateStorageDetailView):
    model = Entrega
    model_file_field = 'memoria'

    #FIXME
    #def get_queryset(self):
    #    # Make sure only certain objects can be accessed.
    #    # Filter only the files that belong to that entrega and belong to self.request.user
    #    return super().get_queryset().filter(...) 

    def can_access_file(self, private_file):
        # When the object can be accessed, the file may be downloaded.
        # This overrides PRIVATE_STORAGE_AUTH_FUNCTION. This should return 
        #     True if user should not be able to download of
        #     False if user should not be able to download
        is_loggedin = (not self.request.user.is_anonymous) and self.request.user.is_authenticated
        is_tribunal = False #ToDo
        is_secretaria = False #ToDo
        is_owner = self.object.matricula.persona.user.pk == private_file.request.user.pk
        return is_loggedin and (is_owner or is_tribunal or is_secretaria)
@login_required
def delete_Entrega(request, pk):
	""" Deletes the Entrega, if exists and belongs to the user """
	e = get_object_or_404(Entrega, pk=pk)
	if not e.matricula.persona.user == request.user:
		return render(request, 'envio/base.html', {'avisos': _("Solo puedes borrar tus propias Entregas")})
	# if Entrega exists and belongs to the user...
	e.delete()
	return HttpResponseRedirect(reverse('list_all_entregas'))


@login_required
def edit_or_create_Entrega(request, pk=None):
	""" Shows the form to create/edit Entrega's """
	if request.method == "POST" and not pk:
		# create form instance and populate it with data from the request
		form = EntregaForm(request.POST, request.FILES)
		if form.is_valid():
			nueva_entrega = form.save()
			return HttpResponseRedirect(reverse('list_all_entregas'))
	elif request.method == "POST" and pk:
		# create form instance and populate it with data from the request AND the existing Entrega
		e = get_object_or_404(Entrega,pk=pk)
		if not e.matricula.persona.user==request.user:
			return render(request, 'envio/base.html', {'avisos': _("Solo puedes editar tus propias Entregas")})
		else:
			form = EntregaForm(request.POST, request.FILES, instance=e)
			if form.is_valid():
				edit_entrega = form.save()
				return HttpResponseRedirect(reverse('list_all_entregas'))
	elif not pk:
		# if a GET (or any other method) and no pk is provided, we'll create a blank form
		form = EntregaForm()

		# we'll limit the Matricula choices to the ones that correspond to that nip
		matriculas = Matricula.objects.filter(persona__user=request.user)
		if not matriculas:
			return render(request,'envio/base.html', {'avisos': _("No hay matriculas disponibles")})
		
		# if matriculas available, proceed...
		matriculas_filtered_choices = []
		for matricula in matriculas:
			matriculas_filtered_choices.append([matricula.pk, matricula.get_nombre_estudio()])
		form.fields['matricula'].choices = matriculas_filtered_choices
	else:
		# if GET (or any other method) and pk is provided, we'll fill the form with the existing
		# entrega object value, if it exists and it belongs to the user
		e = get_object_or_404(Entrega,pk=pk)
		if not e.matricula.persona.user==request.user:
			return render(request, 'envio/base.html', {'avisos': _("Solo puedes editar tus propias Entregas")})
		else:
			form = EntregaForm(instance=e)

	return render(request, 'envio/entrega_form.html', {'form': form})


@login_required
def user_view(request):
    """ Muestra la información del usuario """
    persona = get_object_or_404(Persona, user=request.user)
    return render(request, 'envio/persona_detail.html', {'persona': persona})	


#ToDo must be staff, not just logged in!
@login_required
def get_entregas_centro(request): 
	""" Buscar entregas de trabajos ligados a un centro entre una fecha inicial y otra final """

	if not request.user.is_staff:
		return render(request, 'envio/index.html', {'contents': _('A esta funcionalidad solo pueden acceder los administradores'), 'titlepag': 'Gestión de Trabajos'})

	form = EntregasCentroForm()
	if request.method == 'POST':
		# read form data and show results
		form = EntregasCentroForm(request.POST)
		if form.is_valid():

			# check start date
			if 'fecha_ini' in form.cleaned_data.keys():
				fecha_ini = form.cleaned_data['fecha_ini']
			else:
				fecha_ini = None
				errors.append(forms.ValidationError(_("Fecha inicio vacía o con formato incorrecto")))

			# check end date
			if 'fecha_fin' in form.cleaned_data.keys():
				fecha_fin = form.cleaned_data['fecha_fin']
			else:
				fecha_fin = None
				errors.append(forms.ValidationError(_("Fecha fin vacía o con formato incorrecto")))

			if fecha_ini and fecha_fin:
				entregas = Entrega.objects.filter(matricula__plan__centro = request.POST['centro']).filter(fecha__gte=fecha_ini).filter(fecha__lte=fecha_fin)
				return render(request, 'envio/entregas_centro_form.html', {'form': form, 'entregas': entregas})  

	return render(request, 'envio/entregas_centro_form.html', {'form': form})







