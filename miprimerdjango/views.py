import datetime
from django.http import HttpResponse
from django.template import Template, Context


#v1
# def inicio(request):
#     return HttpResponse('Hola soy tu inicio')

def inicio(request):
    archivo = open(r'C:\Users\Usuario\OneDrive\Desktop\coder carlos\mi_primer_django\templates\inicio.html', 'r')
    
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    renderizar_template = template.render(contexto)
    
    return HttpResponse(renderizar_template)

def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista!</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Fecha-actual: {fecha}</h1>')

def saludar(resquest):
    return HttpResponse('Bienvenido/a!!!')

def bienvenida(resquest, nombre, apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')