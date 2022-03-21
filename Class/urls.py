from django.urls import path
from .views import formulario_usuario,busqueda_usuario,formulario_post

urlpatterns = [
    path('usuario/',formulario_usuario,name='formulario'),
    path('Post/',formulario_post,name='formulario_post'),
    path('busqueda-usuario/',busqueda_usuario,name='busqueda_usuario')
]
