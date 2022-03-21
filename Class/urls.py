from django.urls import path
from .views import nuevo_user, form_user

urlpatterns = [
    path('nuevo/',nuevo_user,name='nuevo_usuario'),
    path('usuario/',form_user,name='form_user')
]
