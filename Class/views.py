
from dataclasses import dataclass
from importlib.resources import contents
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from Class.models import User,Post
from Class.forms import Post_form, User_form,User_found


def nuevo_user(request):
    nuevo_user = User(nombre='Laura',apellido='Carrreras',email='laura.s.carreras@gmail.com',tipo= 'admin')
    nuevo_user.save()
    return HttpResponse(f"Se creo el usuario {nuevo_user.nombre} tipo {nuevo_user.tipo}")

#def nuevo_post(request):
#    nuevo_post = User(titulo='Hola',comentarios='Mi nombre es Laura',)
#    nuevo_post.save()
#    return HttpResponse(f"Se creo un nuevo post {nuevo_post.titulo} tipo {nuevo_post.comntario}")


def formulario_usuario(request):
    formulario = User_form()
    
    if request.method == 'POST':
             formulario = User_form(request.POST)
             if formulario.is_valid():
                 data = formulario.cleaned_data
                 nuevo_user= Post(nombre=data['nombre'],apellido=data['apellido'],email=data['email'],tipo= 'web')
                 nuevo_user.save()
                 return render(request,"index/index.html",{'nuevo_usuer':nuevo_user})

    return render(request,"class/form_user.html",{'formulario': formulario})


def formulario_post(request):
    formulario_post = Post_form()

    if request.method == 'POST':
        formulario_post = Post_form(request.POST)
        if formulario_post.is_valid():
            data = formulario_post.cleaned_data
            nuevo_post = Post(title = data ['title'], content = data ['content'] )
            nuevo_post.save()
            return render(request,"index/index.html",{'nuevo_post':nuevo_post})
    
    return render(request,"class/form_post.html",{'formulario_post':formulario_post})

    
   # if request.method == 'POST':
    #         formulario_post = Post_form(request.POST)
    #         if formulario_post.is_valid():
    #             data = formulario_post.cleaned_data
    #             nuevo_post = Post(title=data['titulo'],contents=data['contenido'])
    #             nuevo_post.save()
    #             return render(request,"index/index.html",{'nuevo_post':nuevo_post})



def busqueda_usuario(request):
    usuarios_buscados = User.objects.filter(nombre='Laura')

    dato = request.GET.get('partial_user',None)

    if dato is not None:
        #usuarios_buscados = User.objects.filter(nombre=dato)
        usuarios_buscados = User.objects.filter(nombre__icontains=dato)
    
    buscador = User_found()

    return render(
        request,'Class/found_user.html',
        {
            'buscador':buscador,
            'usuarios_buscados':usuarios_buscados,
            'dato_buscado':dato 
        }
    )

