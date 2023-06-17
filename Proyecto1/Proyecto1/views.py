#Administrador de V I S T A S
from django.http import HttpResponse
from django.template import Template,Context,loader
def saludo(request):
    return HttpResponse("Hola Django equipo Coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola mundo!</h1>")

def miNombrees(self,nombre):
    data = f'Mi nombre es: <h1> {nombre} </h1>' 
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Derick"
    apellido = "Carcamo"
    namelist = ["Gabriel", "Jimena", "Ignacio", "Patricia", "Natalia"]
    
    diccionario = {
        "nombre": nombre,
        "apellido":apellido,
        "namelist": namelist    
    }
#Los que esta con el # es lo mismo a lo otro que esta activo pero mas PRIMITIVO
    #miHtml = open("C:/Users/diebo/OneDrive/Escritorio/Curso de Python/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #miHtml = loader.get_template('template1.html')
    plantilla = loader.get_template('template1.html')   #Para reconocer al html como una template
    #miHtml.close()
    #miContext = Context(diccionario)
    documento = plantilla.render(diccionario) 
    return HttpResponse(documento)

