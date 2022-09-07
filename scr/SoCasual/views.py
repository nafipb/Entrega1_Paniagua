from django.shortcuts import render, redirect
from django.http import HttpResponse
from SoCasual.models import Blusas, Pantalones, Busos, Avatar
from SoCasual.forms import FormularioBusqueda, BlusasFormulario, PantalonesFormulario, BusosFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from SoCasual.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def index (request):
    avatar= Avatar.objects.filter(user=request.user).first()
    listado_productos = Blusas.objects.all()
    if request.GET.get("nombre_blusas"):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Blusas.objects.filter(nombre__icontains = data["nombre_blusas"])
        return render(request, "SoCasual/index.html",{"blusas":listado_productos, "formulario":formulario, "imagen":avatar.imagen.url})     
    else: 
        formulario= FormularioBusqueda()
        return render(request, 'SoCasual/index.html',{"blusas":listado_productos, "formulario": formulario, "imagen":avatar.imagen.url})          
def productos(request):  
    contenido = {"mensaje": "Se constante en tu trabajo",}
    return render(request, "SoCasual/productos.html", contenido) 
def blusas(request):  
    listado_productos = Blusas.objects.all()
    if request.GET.get("nombre_blusas"):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Blusas.objects.filter(nombre__icontains = data["nombre_blusas"])
        return render(request, "SoCasual/blusas.html",{"blusas":listado_productos, "formulario":formulario})     
    else: 
        formulario= FormularioBusqueda()
        return render(request, 'SoCasual/blusas.html',{"blusas":listado_productos, "formulario": formulario})  
def pantalones(request):  
    listado_productos = Pantalones.objects.all()
    if request.GET.get("nombre_pantalones"):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Pantalones.objects.filter(nombre__icontains = data["nombre_pantalones"])
        return render(request, "SoCasual/pantalones.html",{"pantalones":listado_productos, "formulario":formulario})     
    else: 
        formulario= FormularioBusqueda()
        return render(request, 'SoCasual/pantalones.html',{"pantalones":listado_productos, "formulario": formulario})
def busos(request):  
    listado_productos = Busos.objects.all()
    if request.GET.get("nombre_busos"):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Busos.objects.filter(nombre__icontains = data["nombre_busos"])
        return render(request, "SoCasual/busos.html",{"busos":listado_productos, "formulario":formulario})     
    else: 
        formulario= FormularioBusqueda()
        return render(request, 'SoCasual/busos.html',{"busos":listado_productos, "formulario": formulario})
def contacto(request):
    contenido = {"mensaje": "Se constante en tu trabajo",}
    return render(request, "SoCasual/contacto.html", contenido)

def nosotros(request):
    contenido = {"mensaje": "Se constante en tu trabajo",}
    return render(request, "SoCasual/nosotros.html", contenido)

def formulario (request):
    return render(request, "SoCasual/contacto.html")
def info_formulario (request):
    print(request.POST)
    return HttpResponse( f"Mensaje Enviado:{request.POST}")
@login_required
def items(request):  
    contenido = {"mensaje": "Se constante en tu trabajo",}
    return render(request, "SoCasual/items.html", contenido)

def listadoblusas(request):
    listadoblusas= Blusas.objects.all ()

    if request.method == "GET":  
        formulario= BlusasFormulario()

        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Blusas": listadoblusas,
            "formulario":formulario
        }
        return render(request, "SoCasual/listadoblusa.html", context)
    else:
        formulario = BlusasFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            print(data)

            nombre = data.get("nombre")
            talla = data.get("talla")
            precio= data.get("precio")
            imagen = data.get("imagen")
            stock = data.get("stock")
            listadoblusas=Blusas(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
            listadoblusas.save()

        formulario =BlusasFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Blusas": listadoblusas,
            "formulario":formulario
        }
        return(request, "SoCasual/blusa.html",context)
def listadobusos(request):
    listadobusos = Busos.objects.all ()

    if request.method == "GET":  
        formulario= BusosFormulario()

        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Busos": listadobusos,
            "formulario":formulario
        }
        return render(request, "SoCasual/listadobuso.html", context)
    else:
        formulario = BusosFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            print(data)

            nombre = data.get("nombre")
            talla = data.get("talla")
            precio= data.get("precio")
            imagen = data.get("imagen")
            stock = data.get("stock")
            listadobusos=Busos(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
            listadobusos.save()
        formulario =BusosFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Blusos": listadobusos,
            "formulario":formulario
        }
        return(request, "SoCasual/listadobuso.html",context)

def borrar_blusa(request, id_blusa):
    try:
        blusa= Blusas.objects.get(id=id_blusa)     
        blusa.delete()
        return redirect("productos")
    except:
        return redirect("productos")
def actualizar_blusa(request, id_blusa):
    if request.method == "GET":
        formulario = BlusasFormulario()
        contexto = {
            "formulario": formulario
        }
        return render(request, "SoCasual/actualizarblusa.html", contexto)
 
    else:
        formulario = BlusasFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            try:               
                blusa= Blusas.objects.get(id=id_blusa) 

                nombre = data.get("nombre")
                talla = data.get("talla")
                precio= data.get("precio")
                imagen = data.get("imagen")
                stock = data.get("stock")
                listadoblusas=Blusas(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
                listadoblusas.save()
            except:
                return HttpResponse("Error en la actualizacion")

        formulario= BlusasFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Blusas": blusa,
            "formulario":formulario
        }
        return render(request, "SoCasual/listadoblusa.html", context)
def buscar(request):
    blusa_nombre = request.GET.get("blusa", None)
    if not blusa_nombre:
        return HttpResponse("No indicaste ningun nombre")

    blusa_lista = Blusas.objects.filter(nombre__icontains=blusa_nombre)
    return render(request, "Fio/actualizarblusa.html", {"cursos": blusa_lista})
def listadopantalones(request):
    listadopantalones= Pantalones.objects.all ()

    if request.method == "GET":  
        formulario= PantalonesFormulario()

        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Pantalones": listadopantalones,
            "formulario":formulario
        }
        return render(request, "SoCasual/listadopant.html", context)
    else:
        formulario = PantalonesFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            print(data)

            nombre = data.get("nombre")
            talla = data.get("talla")
            precio= data.get("precio")
            imagen = data.get("imagen")
            stock = data.get("stock")
            listadopantalones=Pantalones(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
            listadopantalones.save()

        formulario =PantalonesFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Pantalones": listadopantalones,
            "formulario":formulario
        }
        return redirect ("SoCasual/listado_pant.html",context)
def borrar_pantalones(request, id_pantalon):
    try:
        pantalon= Pantalones.objects.get(id=id_pantalon)     
        pantalon.delete()
        return redirect("productos")
    except:
        return redirect("productos")
def actualizar_pantalones(request, id_pantalon):
    if request.method == "GET":
        formulario = PantalonesFormulario()
        contexto = {
            "formulario": formulario
        }
        return render(request, "SoCasual/actualizarpantalones.html", contexto)
 
    else:
        formulario = PantalonesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            try:               
                pantalon= Pantalones.objects.get(id=id_pantalon) 

                nombre = data.get("nombre")
                talla = data.get("talla")
                precio= data.get("precio")
                imagen = data.get("imagen")
                stock = data.get("stock")
                pantalon=Pantalones(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
                pantalon.save()
            except:
                return HttpResponse("Error en la actualizacion")

        formulario= PantalonesFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Pantalones": pantalon,
            "formulario":formulario
        }
        return render(request, "SoCasual/listadopant.html", context)
def iniciar_sesion(request):
    if request.method =="GET":
        formulario = AuthenticationForm()

        context ={
            "form":formulario
        }
        return render(request, "SoCasual/login.html",context)
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data=formulario.cleaned_data
            usuario = authenticate(username=data.get("username"), password=data.get("password"))
            if usuario is not None:
                login (request, usuario)
                return redirect ("inicio")
            else:
                context= {
                    "error": "Credenciales no validas",
                    "form":formulario
                }
                return render (request, "SoCasual/login.html",context)
        else:
                context= {
                    "error": "Formulario no valido",
                    "form":formulario
                }
                return render (request, "SoCasual/index.html",context)

def registar_usuario(request):
    if request.method == "GET":
        formulario =  UserRegisterForm()
        return render(request,"SoCasual/registro.html", {"form":formulario} )
    else:
        formulario=  UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
        else:
            return render(request,"SoCasual/registro.html", {"form":formulario, "error":"Formulario no valido"} )
@login_required
def editar_usuario(request):
    if request.method =="GET":
        form = UserEditForm(initial={"email": request.user.email, "first_name":request.user.first_name, "last_name": request.user.last_name})
        return render(request, "SoCasual/update_user.html",{"form":form})
    else:
        form= UserEditForm(request.POST)

        if form.is_valid():
            data=form.cleaned_data

            usuario = request.user

            usuario.email=data["email"]
            usuario.password1=data["password1"]
            usuario.password1=data["password2"]
            usuario.first_name=data ["first_name"]
            usuario.last_name=data ["last_name"]

            usuario.save()
            return redirect("inicio")
        else:
            return render(request, "SoCasual/update_user.html",{"form":form})
@login_required
def agregar_avatar (request):
    if request.method == "  POST":
        form= AvatarForm(request.POST, request.FILES) 
        if form.is_valid():
            data = form.cleaned_data
            usuario= User.objects.get(username=request.user.username)
            avatar = Avatar(user=usuario, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return redirect ("inicio")
    else:
        return render(request, "SoCasual/agregar_avatar.html",context)
def urlImagen():
    return "media/avatares/angelica_picles.JPG"