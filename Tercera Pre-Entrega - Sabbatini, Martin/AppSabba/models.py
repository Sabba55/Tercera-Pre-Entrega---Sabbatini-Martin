from django.db import models

# Create your models here.


#cada una de estas, son columnas :)
#creo mi class estudiantes
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()


#creo mi class curso
class Cursos(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()


#creo mi class profesor
class Profesores(models.Model):
    nombre = models.CharField(max_length=40) #mensajes de texto (cadenas de caract.)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=35)
    edad = models.IntegerField(default=0)