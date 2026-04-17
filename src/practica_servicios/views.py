from django.shortcuts import render
# from practica_servicios import models


def index(request):
    return render(request, "practica_servicios/index.html")
