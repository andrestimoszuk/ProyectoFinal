from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils import timezone

class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Email:")
    apellido = forms.CharField(label='Apellido:')
    nombre = forms.CharField(label='Nombre:')
    usuario = forms.CharField(label='Usuario:')
    pagina_web = forms.CharField(label='Pagina web:')
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['usuario', 'nombre', 'apellido', 'email', 'pagina_web', 'imagen']

class Form_Blog(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.TextInput()
    autor = forms.CharField(max_length=40)
    fecha = forms.DateField()

class Form_Registro(UserCreationForm):
    email = forms.EmailField()