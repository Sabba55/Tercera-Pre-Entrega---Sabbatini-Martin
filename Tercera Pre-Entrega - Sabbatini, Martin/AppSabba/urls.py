from django.urls import path
from AppSabba.views import *

urlpatterns = [
    path("inicio/", inicio, name="Start"),
    path("ver_cursos/", cursos, name="cursos"),
    path("ver_profesores/", profesores, name="profes"),
    path("ver_estudiantes/", estudiantes, name="estudiantes"),

    #~~~~~~~~~~~ APARTADO DE CREACION ~~~~~~~~~~~
    path("crear_estudiantes/", crear_estudiantes, name="Crear Estudiantes"), #botones name del nav
    path("crear_cursos/", crear_cursos, name="Crear Cursos"),

    #~~~~~~~~~~~ APARTADO DE BUSQUEDA EN LA BD ~~~~~~~~~~~
    path("buscar_estudiante/", busquedaEstudiantes, name="Buscar Estudiante"),
    path("resultados_busqueda/", resultadosBusquedaEstudiantes, name="Buscar Estudiantes"),

    path("buscar_curso/", busquedaCursos, name="Buscar Curso"),
    path("resultado_busqueda_cursos/", resultadosBusquedaCursos, name="Buscar Cursos")
]