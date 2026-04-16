from django.urls import path
from practica_servicios import views

app_name = 'practica_servicios'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('servicios/', views.servicios, name='servicios'),
    path('pedidos/', views.pedidos, name='pedidos'),
]