from lib2to3.refactor import MultiprocessingUnsupported
from sqlite3 import Timestamp
from statistics import mode
from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)  
    email = models.EmailField()
    tipo = models.CharField(max_length=10)  

class Post(models.Model):
     title = models.CharField(max_length=100) 
     content = models.TextField()
     publish_date = models.DateTimeField(auto_now_add=True)
     last_upda = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    Timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()