from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Libro, Usuario
from .forms import LibroForm, RegistroUsuarioForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def bienvenida_usuario(request):
    return render(request, 'core/bienvenida_usuario.html')

def libro_lista(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
     }
    return render(request, 'core/libro_lista.html', datos)


def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = LibroForm()
            messages.add_message(request, messages.INFO, 'Registro Creado Correctamente.')
            return  redirect(to="libro_lista")
        else:
            datos['mensaje'] = "ISBN Incorrecto"
    return render(request, 'core/form_libro.html', datos)


def form_mod_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    datos = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            messages.add_message(request, messages.INFO, 'Registro Actualizado Correctamente.')
            return  redirect(to="libro_lista")
    return render(request, 'core/form_mod_libro.html', datos)

def form_del_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    libro.delete()
    messages.add_message(request, messages.INFO, 'Registro Eliminado Correctamente.')
    return redirect(to="libro_lista")

def form_registro_usuario(request):
    datos = {
        'form': RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = RegistroUsuarioForm()
            datos['mensaje'] = "Datos Ingresados correctamente"
            return redirect(to="bienvenida_usuario")
        else:
            datos['mensaje'] = "Incorrecto"
    return render(request, 'core/form_registro_usuario.html', datos)


