from django.urls import path
from .views import nuevo_user

urlpatterns = [
    path('nuevo/',nuevo_user,name='nuevo_usuario')
]
