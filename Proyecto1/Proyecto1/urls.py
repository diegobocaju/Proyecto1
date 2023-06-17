"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo
from Proyecto1.views import segunda_vista
from Proyecto1.views import miNombrees
from Proyecto1.views import probandoTemplate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #Esto es para traer lo del view
# La primera parte del path es el nombre, que puede ir cualquiera, la segunda es la funcion que tiene que ir el mismo nombre
    path('segunda_vista/',segunda_vista),
    path('miNombrees/<nombre>',miNombrees), #Con ese '/<Nombre> lo que haces es que cuando pones el URL lo siguiente seria 
                                           #miNombrees/y tu nombre" y ahi te aparece todo el mensaje deseado.
    path('probandoTemplate/',probandoTemplate)
]
#Cuando va a produccion todo eso de "path..." se saca. Ya que con eso accedemos al admin
#Para ingresar a la parte de "saludo" se debe colocar un "/saludo" luego del URL

