from django.test import TestCase, Client

# Create your tests here.
from .models import Centro, Estudio, Plan
from django.urls import reverse


def create_centro(cid, nombre, url, localidad):
	""" Crea un centro """
	return Centro.objects.create(cid=cid, nombre=nombre, localidad=localidad, url=url)


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


class PlanModelTests(TestCase):

    def test_no_plan(self):
        """
        Si no hay centros en la BD, muestra un mensaje adecuado
        """
        response = self.client.get(reverse('list_all_planes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay planes en la base de datos.")
        self.assertQuerysetEqual(response.context['planes'], [])



