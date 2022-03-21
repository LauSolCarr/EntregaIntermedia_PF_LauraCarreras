from django.urls import path
from .views import formulario_usuario

urlpatterns = [
    path('usuario/',formulario_usuario,name='formulario')
]
