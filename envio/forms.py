from django.forms import ModelForm, Textarea, TextInput
from .models import Entrega, Persona
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django import forms

class EntregaForm(ModelForm):
    """ Modela un formulario para realizar Entregas """
    
    terminos = forms.BooleanField(required=True, help_text=_('Debes aceptar los <button id="toggleTermsAndConditions">Términos y Condiciones</button> para poder realizar la Entrega. <div id="termsandconditions"></div>'))
    
    class Meta:
        model = Entrega
        fields = ['matricula', 'titulo', 'resumen',  'resumen_en', 'notas', 'departamentos', 'entrega_material_adicional', 'memoria', 'anexos', 'license', 'anexos']
        widgets = {'resumen': Textarea(attrs={'cols': 80, 'rows': 15}),
                   'resumen_en': Textarea(attrs={'cols': 80, 'rows': 15}),
                   'notas': Textarea(attrs={'cols': 80, 'rows': 10}),
                   'titulo': TextInput(attrs={'size':80}),
                }
        labels={
            'matricula': _('Estudio'),
            'titulo': _('Título de tu Trabajo'),
            'resumen': _('Resumen (español)'),
            'resumen_en': _('Resumen (inglés)'),
            'memoria': _('Memoria'),
            'anexos': _('Anexos'),
            'ficheroprivado': _('Prueba private files'),
            'entrega_material_adicional': _('Entrega material adicional'),
            'notas': _('Notas'),
            'departamentos': _('Departamento(s)'),
            'terminos': _('Términos y condiciones'),
            'license': _('Licencia'),
        }

        help_texts={
            'memoria': _('La memoria en formato PDF es obligatoria'),
            'anexos': _('Los anexos en formato PDF son opcionales'),
            'titulo': _('El título de tu trabajo. Dale un título descriptivo, no "Trabajo Fin de Grado" o "Trabajo Fin de Máster"'),
            'matricula': _('En caso de que estés matriculado en varios estudios a la vez, elige el estudio para el que vas a realizar tu depósito'),
            'departamentos': _('Elige uno o varios con CTRL/CMD + click'),
            'entrega_material_adicional': _('¿Realizas una entrega física además de la electrónica?'),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']