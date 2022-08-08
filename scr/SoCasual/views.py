from django.shortcuts import render
from django.http import HttpResponse
from SoCasual.models import Blusas
from SoCasual.forms import FormularioBusqueda

# Create your views here.
def index (request):

    listado_productos = Blusas.objects.all()

    if request.GET.get("nombre_blusas"):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():

            data = formulario.cleaned_data
            listado_productos = Blusas.objects.filter(nombre__icontains = data["nombre_blusas"])
        return render(request, "SoCasual/index.html",{"blusas":listado_productos, "formulario":formulario})
        
    else: 
        formulario= FormularioBusqueda()
        return render(request, "SoCasual/index.html",{"blusas":listado_productos, "formulario": formulario})

