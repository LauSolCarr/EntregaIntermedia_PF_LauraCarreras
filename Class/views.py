
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from Class.models import User
from Class.forms import User_form

# Create your views here.

def nuevo_user(request):
    nuevo_user = User(nombre='Laura',apellido='Carrreras',email='laura.s.carreras@gmail.com',tipo= 'admin')
    nuevo_user.save()
    return HttpResponse(f"Se creo el usuario {nuevo_user.nombre} tipo {nuevo_user.tipo}")


def formulario_usuario(request):
    formulario = User_form()
    
    if request.method == 'POST':
             formulario = User_form(request.POST)
             if formulario.is_valid():
                 data = formulario.cleaned_data
                 nuevo_user = User(nombre=data['nombre'],apellido=data['apellido'],email=data['email'],tipo= 'web')
                 nuevo_user.save()
                 return render(request,"index/index.html",{'nuevo_usuer':nuevo_user})

    return render(request,"class/form_user.html",{'formulario': formulario})