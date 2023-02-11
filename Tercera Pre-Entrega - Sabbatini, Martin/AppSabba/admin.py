from django.contrib import admin

#importamos
from AppSabba.models import *

# Register your models here.

#usamos esto y registramos el modelo estudiante en admin
admin.site.register(Estudiante)
admin.site.register(Profesores)
admin.site.register(Cursos)
#esto se relacion con models, osea los def