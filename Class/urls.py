from django.urls import path
from .views import formulario_usuario,busqueda_usuario

urlpatterns = [
    path('usuario/',formulario_usuario,name='formulario'),
    path('busqueda-usuario/',busqueda_usuario,name='busqueda_usuario')
]
