   
from django.urls import path, include
from .views import saludo, segunda_vista, probandoTemplate


urlpatterns = [
   path('saludo/', saludo),
   path('segunda_vista/', segunda_vista),
   path('probandoTemplate/',probandoTemplate)

]

