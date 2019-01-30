from django.test import TestCase, Client

# Create your tests here.
from .models import Centro, Estudio, Plan
from django.urls import reverse


def create_centro(codigo, nombre, url):
	""" Crea un centro """
	return Centro.objects.create(cid=codigo, nombre=nombre, url=url)


class CentroModelTests(TestCase):

    def test_no_centros(self):
        """
        Si no hay centros en la BD, muestra un mensaje adecuado
        """
        response = self.client.get(reverse('list_all_centros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay centros en la base de datos.")
        self.assertQuerysetEqual(response.context['centros'], [])


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



