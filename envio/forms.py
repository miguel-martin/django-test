from django.forms import ModelForm, Textarea
from .models import Entrega, Persona
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django import forms

class EntregaForm(ModelForm):
    """ Modela un formulario para realizar Entregas """

    #def __init__(self, request, *args, **kwargs):
    #    super(Entrega_Form, self).__init__(*args, **kwargs)
    #    self.fields['matricula'].queryset =  Matricula.objects.filter(nip=request.nip)
    
    terminos = forms.BooleanField(required=True, help_text=_('Debes aceptar los Términos y Condiciones para poder realizar la Entrega'))
    
    class Meta:
        model = Entrega
        fields = ['matricula', 'titulo', 'resumen', 'notas', 'departamentos', 'entrega_material_adicional', 'memoria', 'anexos', 'license', 'anexos', 'ficheroprivado']
        widgets = {'resumen': Textarea(attrs={'cols': 80, 'rows': 15}),
                   'notas': Textarea(attrs={'cols': 80, 'rows': 10})
                }
        labels={
            'matricula': _('Estudio'),
            'titulo': _('Título de tu Trabajo'),
            'resumen': _('Resumen (ES)'),
            'memoria': _('Memoria'),
            'anexos': _('Anexos'),
            'ficheroprivado': _('Prueba private files'),
            'entrega_material_adicional': _('Entrega material adicional'),
            'notas': _('Notas'),
            'departamentos': _('Departamento(s)'),
            'terminos': _('Términos y condiciones'),
            'license': _('Licencia'),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']