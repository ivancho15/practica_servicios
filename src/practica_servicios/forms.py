from django import forms
from practica_servicios.models import Cliente, Servicio, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"


class PedidoForm(forms.ModelForm):
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter(disponible_servicio=True)
    )
    
    class Meta:
        model = Pedido
        fields = "__all__"


    def clean_servicio(self):
        # Obtenemos el servicio seleccionado en el formulario
        servicio = self.cleaned_data.get('servicio')

        # Verificamos si el servicio existe y si NO está disponible
        if servicio and not servicio.disponible_servicio:
            raise forms.ValidationError(
                f"El servicio '{servicio.nombre_servicio}' no está disponible actualmente."
            )

        # Siempre debes devolver el valor limpio
        return servicio