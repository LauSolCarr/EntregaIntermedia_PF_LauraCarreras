from django.http import HttpResponse
from django.shortcuts import render
from Class.models import User


# Create your views here.

def nuevo_user(request):
    
    nuevo_user = User(nombre='Laura',apellido='Carrreras',email='laura.s.carreras@gmail.com',tipo= 'admin')
    nuevo_user.save()
    return HttpResponse(f"Se creo el usuario {nuevo_user.nombre} tipo {nuevo_user.tipo}")
