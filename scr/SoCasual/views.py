from django.shortcuts import render
from django.http import HttpResponse
from SoCasual.models import Blusas
from SoCasual.forms import FormularioBusqueda

# Create your views here.
def index (request):


    listado_productos= Blusas.objects.all()

    return render(request, "SoCasual/index.html",{"blusas":listado_productos})

