import re
from django.http import HttpResponse
from django.shortcuts import render
from Class.models import User
from Class.forms import User_form


# Create your views here.

def nuevo_user(request):
    nuevo_user = User(nombre='Laura',apellido='Carrreras',email='laura.s.carreras@gmail.com',tipo= 'admin')
    nuevo_user.save()
    return HttpResponse(f"Se creo el usuario {nuevo_user.nombre} tipo {nuevo_user.tipo}")


def form_user(request):

    if request.method == "POST":
        form = User_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            nuevo_user = User(nombre=data['nombre'],apellido=data['apellido'],email=data['email'],tipo= 'web')
            nuevo_user.save() 

    form = User_form()

    return render(request,"Index/Index.html",{'form' :form})