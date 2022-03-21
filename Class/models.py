from lib2to3.refactor import MultiprocessingUnsupported
from sqlite3 import Timestamp
from statistics import mode
from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)  
    email = models.EmailField()
    tipo = models.CharField(max_length=10)  

    def __str__(self):
        return f"Nombre: {self.nombre}  Apellido: {self.apellido} Email: {self.email} Tipo Usuario: {self.tipo}"

class Post(models.Model):
     title = models.CharField(max_length=100) 
     content = models.TextField()
     publish_date = models.DateTimeField(auto_now_add=True)
     last_upda = models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return f"Titulo: {self.title} Contenido: {self.content} Fecha de Publicaciòn:{self.publish_date} {self.last_upda}"

class Comment(models.Model):
    Timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.Timestamp} {self.content}"