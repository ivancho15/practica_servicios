from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from practica_servicios.models import Cliente
from django.urls import reverse_lazy
from practica_servicios.forms import ClienteForm
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.contrib import messages


# def clientes(request):
#     query = models.Cliente.objects.all()
#     return render(request, "practica_servicios/clientes.html", {"clientes": query})


class ClienteList(ListView):
    model= Cliente
    context_object_name = "clientes"

class ClienteDetail(DetailView):
    model = Cliente
    context_object_name = "cliente"
    
class ClienteDelete(DeleteView):
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy('practica_servicios:cliente_list')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "No se puede eliminar este cliente porque tiene pedidos asociados. Elimine primero los pedidos.")
            return redirect('practica_servicios:cliente_list')

class ClienteCreate(CreateView):
    model= Cliente
    form_class  = ClienteForm
    success_url = reverse_lazy("practica_servicios:cliente_list")

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class  = ClienteForm
    success_url = reverse_lazy("practica_servicios:cliente_list")





