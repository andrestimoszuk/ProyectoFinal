from django.test import TestCase
from Blog.models import Blog
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime

class VerificarRutas(TestCase):
    def test_pagina_inicio(self):
        url = reverse('Inicio')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)

class EliminarBlogTest(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(titulo="miblog", subtitulo="subtitulo", cuerpo="cuerpo", autor="autor", fecha="2024-01-01", imagen="")
        user = get_user_model()
        user.objects.create_superuser("username", password="password")
    
    def test_setup(self):
        """
        Verificar que creo adecuadamente la instancia de blog
        """
        self.assertQuerysetEqual(Blog.objects.filter(titulo__icontains="miblog", subtitulo__icontains="subtitulo").values(), 
                                 [{'id': 1, 'titulo': "miblog", 'subtitulo': "subtitulo", 'cuerpo': "cuerpo", 'autor': "autor", 'fecha': datetime.date(2024, 1, 1), 'imagen': ""}])
    
    def test_login(self):
        """
        Verificar que se inicie sesión como superusuario
        """
        self.assertTrue(self.client.login(username="username", password="password"))
    

    def test_eliminar_blog(self):
        """
        Verificar que se elimine un blog al iniciar sesión como superusuario
        """
        self.client.login(username="username", password="password")
        url = reverse('Borrar_Blog', args=[self.blog.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Blog.objects.filter(titulo__icontains="miblog", subtitulo__icontains="subtitulo"), 
                                 [])

    def test_no_eliminar_blog(self):
        """
        Verificar que NO se elimine un blog sin iniciar sesión
        """
        url = reverse('Borrar_Blog', args=[self.blog.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Blog.objects.filter(titulo__icontains="miblog", subtitulo__icontains="subtitulo").values(), 
                                 [{'id': 1, 'titulo': "miblog", 'subtitulo': "subtitulo", 'cuerpo': "cuerpo", 'autor': "autor", 'fecha': datetime.date(2024, 1, 1), 'imagen': ""}])