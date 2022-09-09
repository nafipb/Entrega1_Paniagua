from django.urls import path
from SoCasual.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/",index, name= "inicio"),
    path("productos/", productos, name= "productos"),
    path("nosotros/", nosotros, name= "nosotros"),
    path("contacto/", contacto, name= "contacto"),
    path("blusas/", blusas, name= "blusas"),
    path("listadoblusas/",blusa, name= "listadoblusas"),
    path("blusas/borrar/<id_blusa>", borrar_blusa, name="borrar_blusa"),
    path("blusas/editar/<id_blusa>", actualizar_blusa, name="actualizar_blusa"),
    path("pantalones/",pantalones, name="pantalones"),
    path("listadopantalones/",listadopantalones, name="listadopantalones"),   
    path("pantalones/borrar/<id_pantalon", borrar_pantalones, name="borrar_pantalon"),
    path("pantalones/editar/<id_pantalon>", actualizar_pantalones, name="actualizar_pantalon"),
    path("busos/", busos, name= "busos"),  
    path("listadobusos/",buso, name="listadobusos"),
    path("borrarbuso/<buso_nombre>", borrar_buso, name="borrar_buso"),
    path("editarbuso/<buso_nombre>", actualizar_buso, name="actualizar_buso"),
    path("infoformulario/", info_formulario, name= "infoformulario"),
    path("items/", items, name="items"), 
    path("resultados/", buscar, name="buscar_blusas"),
    path("iniciar_sesion/",iniciar_sesion, name="iniciar_sesion"),
    path("registrar_usuario/",registar_usuario, name="registrar_usuario"),
    path("salir/",LogoutView.as_view(template_name="SoCasual/logout.html"), name="cerrar_secion"),
    path("editar/",editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name= "agregar_avatar")

]