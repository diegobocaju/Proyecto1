from django.urls import path
from AppCoder.views import inicio,cursos,entregables,estudiantes,profesores

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos), #Esto es para traer lo del view
# La primera parte del path es el nombre, que puede ir cualquiera, la segunda es la funcion que tiene que ir el mismo nombre
    path('entregables/',entregables),
    path('estudiantes/',estudiantes), #Con ese '/<Nombre> lo que haces es que cuando pones el URL lo siguiente seria 
                                           #miNombrees/y tu nombre" y ahi te aparece todo el mensaje deseado.
    path('profesores/',profesores)
]
