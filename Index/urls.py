   
from django.urls import path, include
from .views import inicio, saludo, segunda_vista, probandoTemplate


urlpatterns = [
   path('', inicio),
   path('saludo/', saludo),
   path('segunda_vista/', segunda_vista),
   path('probandoTemplate/',probandoTemplate)

]

