from practica_servicios.models import Servicio
from django.views.generic import ListView


# def servicios(request):
#     query = models.Servicio.objects.all()
#     return render(request, "practica_servicios/servicios.html", {"servicios": query})


class ServicioList(ListView):
    model= Servicio
    context_object_name = "servicios"
    template_name = 'practica_servicios/servicios.html'