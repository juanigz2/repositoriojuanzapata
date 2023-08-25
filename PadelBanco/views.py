from django.shortcuts import render
from .models import Profesores, Turnos, Alumnos
from django.http import HttpResponse
from .forms import profesform, alumnosform

def crear_profe(request):
    nombre_profe="Bruno"
    apellido_profe="San Martin"
    email_profe="bruno@sanmartin.com"
    print("creando profesor")
    profe1=Profesores(nombre=nombre_profe, apellido=apellido_profe, email=email_profe)
    profe1.save()
    respuesta=f"Profesor creado: {profe1.nombre} - {profe1.apellido} - {profe1.email}"
    return HttpResponse(respuesta)



def listar_profes(request):

    profes=Profesores.objects.all()
    respuesta=""
    for profe in profes:
        respuesta+=f"{profe.nombre} - {profe.apellido} - {profe.email}<br>"
    return HttpResponse(respuesta)


def inicio(request):
    return render(request,"PadelBanco/inicio.html")


def turnos(request):
    turno=Turnos.objects.all()

    return render(request,"PadelBanco/turnos.html", {"turnos":turno})

def profesores(request):
    if request.method=="POST":
        form=profesform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profe=Profesores(nombre=nombre, apellido=apellido, email=email)
            profe.save()
            form=profesform()
            return render(request, "PadelBanco/profesores.html", {"mensaje":"Profesor cargado", "formulario":formulario_profes})
        return render(request, "PadelBanco/profesores.html", {"mensaje":"Datos invalidos"})

    else:
         formulario_profes=profesform()
         return render(request,"PadelBanco/profesores.html", {"formulario":formulario_profes})




def alumnos(request):
    if request.method=="POST":
        form=alumnosform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            alumno=Alumnos(nombre=nombre, apellido=apellido, email=email)
            alumno.save()
            formulario_alumnos=alumnosform()
            return render(request, "PadelBanco/alumnos.html", {"mensaje":"Alumno cargado", "formulario":formulario_alumnos})
        return render(request, "PadelBanco/profesores.html", {"mensaje":"Datos invalidos"})

    else:
        formulario_alumnos=alumnosform()

    return render(request,"PadelBanco/alumnos.html", {"formulario":formulario_alumnos})





def busquedaprofesor(request):
    return render(request,"PadelBanco/busquedaprofesor.html")


def buscar(request):
    apellido=request.GET["apellido"]
    if apellido!="":
        profes=Profesores.objects.filter(apellido=apellido)
        return render(request,"PadelBanco/resultadosbusqueda", {"profes":profes})
    else:
        return render(request,"PadelBanco/busquedaprofesor.html", {"mensaje":"Ingrese un profesor activo"})