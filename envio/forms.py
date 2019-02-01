from django.forms import ModelForm
from .models import Entrega


class EntregaForm(ModelForm):
    """ Modela un formulario para realizar Entregas """

    #def __init__(self, request, *args, **kwargs):
    #    super(Entrega_Form, self).__init__(*args, **kwargs)
    #    self.fields['matricula'].queryset =  Matricula.objects.filter(nip=request.nip)

    class Meta:
        model = Entrega
        fields = ['matricula', 'titulo', 'resumen']
        labels={
            'matricula':' Estudio',
            'titulo': 'Título de tu Trabajo',
            'resumen': 'Resumen (ES)',
        }