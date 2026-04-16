from django.shortcuts import render
from practica_servicios import models

def index(request):
    return render(request, "practica_servicios/index.html")

def clientes(request):
    query = models.Cliente.objects.all()
    return render(request, "practica_servicios/clientes.html", {"clientes": query})

def servicios(request):
    query = models.Servicio.objects.all()
    return render(request, "practica_servicios/servicios.html", {"servicios": query})

def pedidos(request):
    query = models.Pedido.objects.all()
    return render(request, "practica_servicios/pedidos.html", {"pedidos": query})

