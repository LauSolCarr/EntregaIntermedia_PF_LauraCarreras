   
from django.urls import path, include
from .views import blog, inicio, saludo, segunda_vista, probandoTemplate


urlpatterns = [
   path('', inicio, name = "inicio"),
   path('blog/', blog , name = "blog"),
   path('saludo/', saludo, name = "saludo"),
   path('segunda_vista/', segunda_vista,name= "segunda_vista" ),
   path('probandoTemplate/',probandoTemplate, name = "probando_template")

]

