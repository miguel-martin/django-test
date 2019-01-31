from django.test import TestCase, Client

# Create your tests here.
from .models import Centro, Estudio, Plan
from django.urls import reverse


def create_centro(cid, nombre, url, localidad):
	""" Crea un centro """
	return Centro.objects.create(cid=cid, nombre=nombre, localidad=localidad, url=url)

def create_estudio(eid, nombre, tipo):
	""" Crea un centro """
	return Estudio.objects.create(eid=eid, nombre=nombre, tipo=tipo)

def create_plan(pid, curso, estudio, centro):
	""" Crea un plan """
	return Plan.objects.create(pid=pid, curso=curso, centro=centro, estudio=estudio)


class CentroModelTests(TestCase):

    def test_no_centros(self):
        """
        Si no hay centros en la BD, muestra un mensaje adecuado
        """
        response = self.client.get(reverse('list_all_centros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay centros en la base de datos.")
        self.assertQuerysetEqual(response.context['centros'], [])

    def test_create_centro_and_view_listing(self):
    	""" 
    	Crea un centro y comprueba que aparece en el listado de centros
    	"""
    	create_centro(cid=110, nombre='Escuela de Ingeniería y Arquitectura', localidad='Z', url='http://eina.unizar.es')
    	response = self.client.get(reverse('list_all_centros'))
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Escuela de Ingeniería y Arquitectura")
    	self.assertQuerysetEqual(
    		response.context['centros'],
    		['<Centro: Escuela de Ingeniería y Arquitectura>']
    	)

    def test_create_centro_and_view_details(self):
    	""" 
    	Crea un centro y comprueba que aparece el detalle del centro
    	"""
    	create_centro(cid=110, nombre='Escuela de Ingeniería y Arquitectura', localidad='Z', url='http://eina.unizar.es')
    	response = self.client.get(reverse('list_centro', kwargs={'pk': 110}))
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Escuela de Ingeniería y Arquitectura")
    	self.assertQuerysetEqual(
    		[response.context['centro']],
    		['<Centro: Escuela de Ingeniería y Arquitectura>']
    	)


class EstudioModelTests(TestCase):

    def test_no_estudios(self):
        """
        Si no hay centros en la BD, muestra un mensaje adecuado
        """
        response = self.client.get(reverse('list_all_estudios'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay estudios en la base de datos.")
        self.assertQuerysetEqual(response.context['estudios'], [])

    def test_create_estudio_and_view_listing(self):
    	""" 
    	Crea un estudio y comprueba que aparece en el listado de estudios
    	"""
    	create_estudio(157, "Graduado en Estudios en Arquitectura", 5)
    	response = self.client.get(reverse('list_all_estudios'))
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Graduado en Estudios en Arquitectura")
    	self.assertQuerysetEqual(
    		response.context['estudios'],
    		['<Estudio: (157) Graduado en Estudios en Arquitectura>']
    	)

    def test_create_estudio_and_view_detail(self):
    	""" 
    	Crea un estudio y comprueba que aparece en el listado de estudios
    	"""
    	create_estudio(157, "Graduado en Estudios en Arquitectura", 5)
    	response = self.client.get(reverse('list_estudio', kwargs={'pk': 157}))	
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Graduado en Estudios en Arquitectura")
    	self.assertQuerysetEqual(
    		[response.context['estudio']],
    		['<Estudio: (157) Graduado en Estudios en Arquitectura>']
    	)


class PlanModelTests(TestCase):

    def test_no_plan(self):
        """
        Si no hay centros en la BD, muestra un mensaje adecuado
        """
        response = self.client.get(reverse('list_all_planes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay planes en la base de datos.")
        self.assertQuerysetEqual(response.context['planes'], [])

    def test_create_plan_and_view_listing(self):
    	""" 
    	Crea un centro/estudio/plan y comprueba que aparece en el listado de planes
    	"""
    	create_centro(cid=110, nombre='Escuela de Ingeniería y Arquitectura', localidad='Z', url='http://eina.unizar.es')
    	create_estudio(157, "Graduado en Estudios en Arquitectura", 5)
    	create_plan(470, curso='2018', estudio=Estudio.objects.get(eid=157), centro=Centro.objects.get(cid=110))
    	response = self.client.get(reverse('list_all_planes'))
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Escuela de Ingeniería y Arquitectura")
    	self.assertContains(response, "Graduado en Estudios en Arquitectura")
    	self.assertQuerysetEqual(
    		response.context['planes'],
    		['<Plan: 470 - (157) Graduado en Estudios en Arquitectura>']
    	)

    def test_create_plan_and_view_detail(self):
    	"""
    	Crea un centro/estudio/plan y comprueba que aparece el detalle del plan
    	"""
    	create_centro(cid=110, nombre='Escuela de Ingeniería y Arquitectura', localidad='Z', url='http://eina.unizar.es')
    	create_estudio(157, "Graduado en Estudios en Arquitectura", 5)
    	create_plan(470, curso='2018', estudio=Estudio.objects.get(eid=157), centro=Centro.objects.get(cid=110))
    	response = self.client.get(reverse('list_plan', kwargs={'pk':470}))
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Escuela de Ingeniería y Arquitectura")
    	self.assertContains(response, "Graduado en Estudios en Arquitectura")
    	self.assertQuerysetEqual(
    		[response.context['plan']],
    		['<Plan: 470 - (157) Graduado en Estudios en Arquitectura>']
    	)

