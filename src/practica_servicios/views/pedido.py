from practica_servicios.models import Pedido
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from practica_servicios.forms import PedidoForm


class PedidoList(ListView):
    model = Pedido
    context_object_name = "pedidos"
    template_name = 'practica_servicios/pedidos.html'


class PedidoDetail(DetailView):
    model = Pedido
    context_object_name = "pedido"
    template_name = 'practica_servicios/pedido_detail.html'


class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'practica_servicios/pedido_form.html'
    success_url = reverse_lazy('practica_servicios:pedidos')


class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'practica_servicios/pedido_form.html'
    success_url = reverse_lazy('practica_servicios:pedidos')


class PedidoDelete(DeleteView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'practica_servicios/pedido_confirm_delete.html'
    success_url = reverse_lazy('practica_servicios:pedidos')
    