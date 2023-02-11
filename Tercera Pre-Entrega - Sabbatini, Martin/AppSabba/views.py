from django.shortcuts import render

#Importamos HttpResponse
from django.http import HttpResponse

#Importamos models y forms para hacer uso de ellas
from AppSabba.models import *
from AppSabba.forms import *

# Create your views here.
#---------------------------------------





#iniciamos con los def :)
def inicio(request): #tomar como un self el request

    return render(request, "AppSabba/inicio.html") #buscamos el archivo en html



def estudiantes(request):
    #metodo para ver estudiantes 
    listaEstudiantes = Estudiante.objects.all()
    return render(request, "AppSabba/ver_Estudiantes.html", {"listaEstudiantes":listaEstudiantes} )

def profesores(request):
    listaProfesores = Profesores.objects.all()
    return render(request, "AppSabba/ver_Profesores.html", {"listaProfesores":listaProfesores} )

def cursos(request):
    listaCursos = Cursos.objects.all()
    return render(request, "AppSabba/ver_Cursos.html", {"listaCursos":listaCursos})






#----------------------------------------------------------------
#zona de creacion
#sirve para guardar la informacion, y el html para almacenar la info
def crear_estudiantes(request): #Crear usando forms de django
    if request.method == 'POST':

        miFormulario = EstudianteFormulario(request.POST)

        if miFormulario.is_valid():
            infoDict = miFormulario.cleaned_data
            estudiante1 = Estudiante(nombre = infoDict['nombre'],
                                    apellido = infoDict['apellido'],
                                    email = infoDict['email'])
            estudiante1.save()

            return render(request, "AppSabba/inicio.html")

    else: #si no le doy click
        miFormulario = EstudianteFormulario()
    return render(request, "AppSabba/crearEstudiantes.html", {"formulario1":miFormulario})



def crear_cursos(request): #Crear usando forms de django
    if request.method == 'POST':  #guarda los datos y crea el curso con el boton enviar

        miFormulario = CursoFormulario(request.POST) #lee la informacion dentro del form


        if miFormulario.is_valid(): #validar que este todo ok los datos

            infoDict = miFormulario.cleaned_data #la info del form se pasa a tipo diccionario

            curso1 = Cursos(nombre = infoDict["nombre"],
                           comision = infoDict["comision"])

            curso1.save()

            return render(request, "AppSabba/inicio.html")
    
    else: #si no le doy click
        miFormulario = CursoFormulario()

    return render(request, "AppSabba/crearCursos.html", {"formulario1":miFormulario})

#-------------------------------- ZONA DE BUSQUEDA --------------------------------
#ESTUDIANTES
def busquedaEstudiantes(request):
    return render(request, "AppSabba/busquedaEstudiantes.html")


def resultadosBusquedaEstudiantes(request):
    if request.method == "GET":

        estudiantesBusqueda = request.GET["apellido"]
        estudiantesResultados = Estudiante.objects.filter(apellido__icontains=estudiantesBusqueda) #pedimos todo su contenido, lo filtramos
        
        return render(request, "AppSabba/resultadosBusquedaEstudiantes.html", {"apellido":estudiantesBusqueda, "resultado":estudiantesResultados})

    return render(request, "AppSabba/resultadosBusquedaEstudiantes.html")


#CURSOS
def busquedaCursos(request):
    return render(request, "AppSabba/busquedaCursos.html")


def resultadosBusquedaCursos(request):
    if request.method == "GET":

        cursoBusqueda = request.GET["nombre"]
        cursoResultados = Cursos.objects.filter(nombre__icontains=cursoBusqueda) #pedimos todo su contenido, lo filtramos
        
        return render(request, "AppSabba/resultadosBusquedaCursos.html", {"nombre":cursoBusqueda, "resultado":cursoResultados})

    return render(request, "AppSabba/resultadosBusquedaCursos.html")