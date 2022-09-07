from django.urls import path
from SoCasual.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/",index, name= "inicio"),
    path("productos/", productos, name= "productos"),
    path("nosotros/", nosotros, name= "nosotros"),
    path("contacto/", contacto, name= "contacto"),
    path("blusas/", blusas, name= "blusas"),
    path("pantalones/",pantalones, name="pantalones"),
    path("busos/", busos, name= "busos"),
    path("infoformulario/", info_formulario, name= "infoformulario"),
    path("items/", items, name="items"),
    path("listadoblusas/",listadoblusas, name= "listadoblusas"),
    path("blusaborrar/<id_blusa>", borrar_blusa, name="borrar_blusa"),
    path("blusaeditar/<id_blusa>", actualizar_blusa, name="actualizar_blusa"),
    path("listadopantalones/",listadopantalones, name="listadopantalones"),   
    path("pantalonborrar/<id_pantalon", borrar_pantalones, name="borrar_pantalones"),
    path("pantaloneditar/<id_pantalon>", actualizar_pantalones, name="actualizar_pantalones"),
    path("listadobusos/",listadobusos, name="listadobusos"),
    path("resultados/", buscar, name="buscar_blusas"),
    path("iniciar_sesion/",iniciar_sesion, name="iniciar_sesion"),
    path("registrar_usuario/",registar_usuario, name="registrar_usuario"),
    path("salir/",LogoutView.as_view(template_name="SoCasual/logout.html"), name="cerrar_secion"),
    path("editar/",editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name= "agregar_avatar")

]