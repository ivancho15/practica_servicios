from django.views.generic import ListView, DetailView
from practica_servicios.models import Cliente


# def clientes(request):
#     query = models.Cliente.objects.all()
#     return render(request, "practica_servicios/clientes.html", {"clientes": query})


class ClienteList(ListView):
    model= Cliente
    context_object_name = "clientes"

class ClienteDetail(DetailView):
    model = Cliente
    context_object_name = "cliente"
    