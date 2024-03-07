"""
URL configuration for Clase10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Blog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.Login_Usuario, name="Login"),
    path('signup', views.registro, name="Registro"),
    path('logout', LogoutView.as_view(template_name='Blog/logout.html', ), name="Logout"),
    path('profile', views.Editar_Perfil, name="EditarPerfil"), 
    path('password', views.CambiarClave.as_view(), name="CambiarClave"),
    path('', views.inicio, name="Inicio"),
    path('new', views.Crear_Blog.as_view(), name="Nuevo_Blog"),
    path('pages/<pk>', views.Detallar_Blog.as_view(), name="Detalle_Blog"),
    path('pages/<pk>/editar', views.Editar_Blog.as_view(), name="Editar_Blog"),
    path('pages/<pk>/borrar', views.Borrar_Blog.as_view(), name="Borrar_Blog"),
    path('sucess', views.suceso, name="Suceso"),
    path('about', views.about, name="About"),
    path('blogs', views.Listar_Blogs.as_view(), name="Lista_Blogs")
]