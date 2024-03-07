# Generated by Django 5.0.1 on 2024-03-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_profesor_email_alter_profesor_profesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(max_length=40)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]