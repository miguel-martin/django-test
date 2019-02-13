from django.forms import ModelForm, Textarea
from .models import Entrega, Persona
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class EntregaForm(ModelForm):
    """ Modela un formulario para realizar Entregas """

    #def __init__(self, request, *args, **kwargs):
    #    super(Entrega_Form, self).__init__(*args, **kwargs)
    #    self.fields['matricula'].queryset =  Matricula.objects.filter(nip=request.nip)
    
    class Meta:
        model = Entrega
        fields = ['matricula', 'titulo', 'resumen', 'notas', 'entrega_material_adicional', 'memoria', 'anexos', 'terminos']
        widgets = {'resumen': Textarea(attrs={'cols': 80, 'rows': 15}),
                   'notas': Textarea(attrs={'cols': 80, 'rows': 10})
                }
        labels={
            'matricula': _('Estudio'),
            'titulo': _('Título de tu Trabajo'),
            'resumen': _('Resumen (ES)'),
            'memoria': _('Memoria'),
            'anexos': _('Anexos'),
            'entrega_material_adicional': _('Entrega material adicional'),
            'notas': _('Notas'),
            'terminos': _('Términos y condiciones'),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']