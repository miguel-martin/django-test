from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """ Renders a sample index page """
    return render(request, 'base.html', {'contents': 'My first app', 'titulo': 'Página ppal'})
