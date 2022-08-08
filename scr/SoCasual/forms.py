from django.forms import Form, CharField, IntegerField, FileField,FloatField

#Formulario de busqueda para buscar cosas 

class FormularioBusqueda(Form):
    nombre_producto = CharField(max_length=150)