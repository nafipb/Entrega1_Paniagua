from django.forms import Form, CharField, IntegerField, ImageField,FloatField, EmailField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario de busqueda para buscar cosas 

class FormularioBusqueda(Form):
    nombre= CharField(max_length=150)

class BlusasFormulario(Form):
    nombre= CharField()
    talla= CharField()
    precio= FloatField()
    imagen=ImageField()
    stock=IntegerField()

class PantalonesFormulario(Form):
    nombre= CharField()
    talla= CharField()
    precio= FloatField()
    imagen=ImageField()
    stock=IntegerField()

class BusosFormulario(Form):
    nombre= CharField()
    talla= CharField()
    precio= FloatField()
    imagen=ImageField()
    stock=IntegerField()
    
class MediasFormulario(Form):
    nombre= CharField()
    talla= CharField()
    precio= FloatField()
    imagen=ImageField()
    stock=IntegerField()

class UserRegisterForm(UserCreationForm):
    email= EmailField()
    password1= CharField(label= "Contraseña", widget=PasswordInput)
    password2= CharField(label= "Confirmar Contraseña", widget=PasswordInput)
    class Meta:
        model= User
        fields=["username", "email", "password1", "password2"]
        help_texts = {"username": "No mas de 15 caracteres" , "email": "", "password1": " Debe llevar: Mayuscula, minuscula, numeros y simbolo", "password2":""}

class UserEditForm(UserCreationForm):
    first_name=CharField(label="nombre")
    last_name=CharField(label="apellido")
    email= EmailField()
    password1= CharField(label= "Nueva Contraseña", widget=PasswordInput)
    password2= CharField(label= "Confirmar Contraseña", widget=PasswordInput)  
    class Meta:
        model= User
        fields=["first_name", "last_name","email", "password1", "password2"]
        help_texts = { "email": "", "password1": " Debe llevar: Mayuscula, minuscula, numeros y simbolo", "password2":""}
class AvatarForm(Form):
    imagen=ImageField()