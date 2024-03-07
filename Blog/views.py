from django.shortcuts import render
from django.urls import reverse_lazy
from Blog import forms, models
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView

def suceso(request):
    return render(request, 'Blog/mensaje.html')

def about(request):
    return render(request, 'Blog/about.html')

def inicio(request):
    return render(request, 'Blog/inicio.html')

# Vista de registro de usuario
def registro(request):
    if request.method == 'POST':
        form = forms.Form_Registro(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"Blog/mensaje.html" ,  {"mensaje":"Usuario Creado"})
    else:
            form = forms.Form_Registro()     
    return render(request,"Blog/registro.html" ,  {"form":form})

def Login_Usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            login(request, user)            
            return render(request, "Blog/mensaje.html", {"mensaje": f'Bienvenido {user.username}'})         
    else:
        form = AuthenticationForm()
    return render(request, "Blog/login.html", {"form": form})

# Vista de editar el perfil
@login_required
def Editar_Perfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    models.Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request,"Blog/mensaje.html" ,  {"mensaje":"Se ha actualizado su perfil"})
    else:
        miFormulario = forms.UserEditForm(instance=request.user)
    return render(request, "Blog/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'Blog/cambiar_clave.html'
    success_url = reverse_lazy('EditarPerfil')

class Crear_Blog(CreateView):
    model = models.Blog
    template_name = "Blog/blog_crear.html"
    success_url = reverse_lazy('Lista_Blogs')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'fecha', 'autor']

class Listar_Blogs(ListView):
    model = models.Blog
    context_object_name = "blogs"
    template_name = "Blog/blogs_lista.html"
    
class Detallar_Blog(DetailView):
    model = models.Blog
    template_name = "Blog/blog_detalle.html"
    success_url = reverse_lazy('Lista_Blogs')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

class Editar_Blog(LoginRequiredMixin, UpdateView):
    model = models.Blog
    template_name = "Blog/blog_editar.html"
    success_url = reverse_lazy('Lista_Blogs')
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

class Borrar_Blog(LoginRequiredMixin, DeleteView):
    model = models.Blog
    template_name = "Blog/blog_borrar.html"
    success_url = reverse_lazy('Lista_Blogs')
