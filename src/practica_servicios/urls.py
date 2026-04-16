from django.urls import path
from django.views.generic import TemplateView
from practica_servicios.views import  cliente, servicio, pedido

app_name = 'practica_servicios'

urlpatterns = [
    path('', TemplateView.as_view(template_name="practica_servicios/index.html"), name='index'),
    path('clientes/', cliente.ClienteList.as_view(), name='cliente_list'),
    path('servicios/', servicio.ServicioList.as_view(), name='servicios'),
    path('pedidos/', pedido.PedidoList.as_view(), name='pedidos'),
    path('clientes/detail/<int:pk>', cliente.ClienteDetail.as_view(), name='cliente_detail'),
]