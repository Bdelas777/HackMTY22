from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.
# Boostrap formatos css  y es responsive compatible para todos los navegadores
''' Crear una web bien organizada
reutilizacion de elementos web
diseño adaptable
crea grids
comunidad activa
uso en cms
uso de less'''

def home(request):
    carro = Carro(request)
    return render(request, "ProyectoWebapp/home.html")


