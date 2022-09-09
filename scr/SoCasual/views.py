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
def blusa(request): # Para añadir items de Blusas
    blusa= Blusas.objects.all ()
    if request.method == "GET":  
        formulario= BlusasFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "blusa": blusa,
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
            
            blusa=Blusas(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
            blusa.save()
            formulario = BlusasFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "blusas": blusa,
            "formulario":formulario
        }
        return render (request, "SoCasual/blusas.html",context)

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

                blusa=Blusas(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
                blusa.save()
            except:
                return HttpResponse("Error en la actualizacion")
        return redirect("productos")
       
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
def listadopantalones(request):   
    pantalon= Pantalones.objects.all() 
    if request.method == "GET":  
        formulario= PantalonesFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Pantalon": pantalon,
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
            pantalon=Pantalones(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
            pantalon.save()

        formulario =PantalonesFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Pantalon": pantalon,
            "formulario":formulario
        }
        return render (request, "SoCasual/pantalones.html",context)
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
        return redirect("productos")
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
def buso(request):
    buso = Busos.objects.all ()
    if request.method == "GET":  
        formulario= BusosFormulario()

        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Buso": buso,
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
            buso=Busos(nombre=nombre, talla=talla, precio=precio, imagen=imagen, stock=stock) 
            buso.save()
        formulario =BusosFormulario()
        context = {
            "mensaje": "Esta pagina es accesada solo por el dueño para añadir nuevos items",
            "Busos": buso,
            "formulario":formulario
        }
    return render (request, "SoCasual/istadobuso.html",context)

def borrar_buso(request, id_buso):
    try:
        buso= Busos.objects.get(id=id_buso)     
        buso.delete()
        return redirect("productos")
    except:
        return redirect("productos")
def actualizar_buso(request, buso_nombre):
    buso= Busos.object.get (nombre=buso_nombre)
    if request.method == "POST":
        formulario = BusosFormulario( request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            buso.nombre = informacion['nombre']
            buso.talla = informacion ['talla']
            buso.precio= informacion['precio']
            buso.imagen = informacion ['imagen']
            buso.stock= informacion ['stock']
            buso.save()
            return redirect("productos")
    else:
        formulario = BusosFormulario(initial = {'nombre': buso.nombre, 'talla': buso.talla, 'precio': buso.precio, 'imagen': buso.imagen, 'stock': buso.stock})
    return redirect ('actualizar_buso')
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
def buscar(request):
    blusa_nombre = request.GET.get("blusa", None)
    if not blusa_nombre:
        return HttpResponse("No indicaste ningun nombre")

    blusa_lista = Blusas.objects.filter(nombre__icontains=blusa_nombre)
    return render(request, "Fio/actualizarblusa.html", {"cursos": blusa_lista})
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
        return render(request, "SoCasual/agregar_avatar.html")
def urlImagen():
    return "media/avatares/angelica_picles.JPG"