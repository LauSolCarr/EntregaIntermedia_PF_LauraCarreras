from django.urls import path
from .views import formulario_comentario, formulario_usuario,busqueda_usuario,formulario_post, formulario_comentario

urlpatterns = [
    path('usuario/',formulario_usuario,name='formulario'),
    path('Post/',formulario_post,name='formulario_post'),
    path('Comment/',formulario_comentario,name='formulario_comentario'),
    path('busqueda-usuario/',busqueda_usuario,name='busqueda_usuario')
]
