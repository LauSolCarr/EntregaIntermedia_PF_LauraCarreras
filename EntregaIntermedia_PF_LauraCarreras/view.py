from datetime import datetime
from importlib.abc import Loader
from pipes import Template
from re import template
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Context,Template, loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br> <br> < a entendimos esto es muy simple :) ")

def dia_de_hoy (request):
    
    dia = datetime.now()

    documentotexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentotexto)

def MyNombreEs (self,nombre):

    documentotexto = f"Mi nombre es: {nombre}"

    return HttpResponse(documentotexto)

def probandoTemplate (request):

    nombre = 'Laura'
    apellido = 'Carreras'

    diccionario = {
        "nombre" : nombre , 
        "apellido" : apellido,
        "nombre_largo" : len(nombre)
        }

    template = loader.get_template("template1.html")

    documento = template.render(diccionario)
    
    return HttpResponse(documento)

