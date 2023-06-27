from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Perro
from django.shortcuts import render



#v1
# def inicio(request):
#     return HttpResponse('Hola soy tu inicio')

#v2
# def inicio(request):
#     archivo = open(r'C:\Users\Usuario\OneDrive\Desktop\coder carlos\mi_primer_django\templates\inicio.html', 'r')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25))
#     }
#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)
 
 #v3
 
# def inicio(request):
#     # archivo = open(r'C:\Users\Usuario\OneDrive\Desktop\coder carlos\mi_primer_django\templates\inicio.html', 'r')
#     # template = Template(archivo.read())
#     # archivo.close()
    
#     template = loader.get_template('inicio.html')
    
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25))
#     }
#     # contexto = Context(diccionario)
#     # renderizar_template = template.render(contexto)
    
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

# def segunda_vista(request):
#     return HttpResponse('<h1>Soy la segunda vista!</h1>')

# def fecha_actual(request):
#     fecha = datetime.now()
#     return HttpResponse(f'<h1>Fecha-actual: {fecha}</h1>')

# def saludar(resquest):
#     return HttpResponse('Bienvenido/a!!!')

# def bienvenida(resquest, nombre, apellido):
#     return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')

# def crear_perro(resquest, nombre, edad):
#     template = loader.get_template('inicio.html')
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro,
#     }
 
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

#v4
def prueba(request):   
    # template = loader.get_template('inicio.html')
    
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25))
    }
    
    # renderizar_template = template.render(diccionario)
    # return HttpResponse(renderizar_template)
    return render(request, 'inicio/prueba.html', diccionario)

def inicio(request):
    return render(request, 'inicio/inicio.html')

def segunda_vista(request):
        return HttpResponse('<h1>Soy la segunda vista!</h1>')

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Fecha-actual: {fecha}</h1>')

def saludar(resquest):
    return HttpResponse('Bienvenido/a!!!')

def bienvenida(resquest, nombre, apellido):
    return HttpResponse(f'Bienvenido/a {nombre.title()} {apellido.title()}!!!')

#v1
# def crear_perro(resquest, nombre, edad):
#     template = loader.get_template('inicio.html')
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro,
#     }

#v2    
def crear_perro(resquest, nombre, edad):
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
    'perro': perro,
    }
    return render(resquest, 'inicio/crear_perro.html', diccionario)
