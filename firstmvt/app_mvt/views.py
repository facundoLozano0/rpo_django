from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from app_mvt.models import familiares
from django.template import loader
# Create your views here.
def familiaress(request):
    flia= familiares.objects.all()
    dicc= {'familiares:': familiaress}
    plantillas= loader.get_template('plantilla.html')
    documento= plantillas.render(dicc)
    return HttpResponse(documento)

def abuela(request):
    abu=familiares(nombre='Ester', camada=321321, fecha='1975-5-7')
    abu.save()
    texto=f'mi abuela se llama {abu.nombre}, y nacio en el {abu.fecha} '
    return HttpResponse(texto)

def tios(request):
    tio=familiares(nombre='cacho', camada=123546, fecha='1985-2-8')
    tio.save()
    texto=f'mi abuela se llama {tio.nombre}, y nacio en {tio.fecha}'
    return HttpResponse(texto)

def primos(request):
    primo=familiares(nombre='fabri', camada=56489, fecha='2003-7-12')
    primo.save()
    texto=f'el nombre de mi primo es {primo.nombre} y nacio en {primo.fecha}'
    return HttpResponse(texto) 