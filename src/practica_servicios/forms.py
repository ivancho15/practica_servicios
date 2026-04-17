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
    class Meta:
        model = Pedido
        fields = "__all__"