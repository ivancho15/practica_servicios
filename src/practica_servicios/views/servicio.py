from practica_servicios.models import Servicio
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from practica_servicios.forms import ServicioForm
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.contrib import messages


# def servicios(request):
#     query = models.Servicio.objects.all()
#     return render(request, "practica_servicios/servicios.html", {"servicios": query})


class ServicioList(ListView):
    model = Servicio
    context_object_name = "servicios"
    template_name = 'practica_servicios/servicios.html'


class ServicioDetail(DetailView):
    model = Servicio
    context_object_name = "servicio"
    template_name = 'practica_servicios/servicio_detail.html'


class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'practica_servicios/servicio_form.html'
    success_url = reverse_lazy('practica_servicios:servicios')


class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'practica_servicios/servicio_form.html'
    success_url = reverse_lazy('practica_servicios:servicios')


class ServicioDelete(DeleteView):
    model = Servicio
    context_object_name = 'servicio'
    template_name = 'practica_servicios/servicio_confirm_delete.html'
    success_url = reverse_lazy('practica_servicios:servicios')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "No se puede eliminar este Servicio porque tiene pedidos asociados. Elimine primero los pedidos.")
            return redirect('practica_servicios:servicios')