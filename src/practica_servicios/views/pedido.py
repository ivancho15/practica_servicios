from  practica_servicios.models import Pedido
from django.views.generic import ListView


# def pedidos(request):
    # query = models.Pedido.objects.all()
    # return render(request, "practica_servicios/pedidos.html", {"pedidos": query})


class PedidoList(ListView):
    model= Pedido
    context_object_name = "pedidos"
    template_name = 'practica_servicios/pedidos.html'
    