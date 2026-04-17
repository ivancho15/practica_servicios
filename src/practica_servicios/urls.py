from django.urls import path
from django.views.generic import TemplateView
from practica_servicios.views import cliente, servicio, pedido

app_name = "practica_servicios"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="practica_servicios/index.html"),
        name="index",
    ),
    path("clientes/", cliente.ClienteList.as_view(), name="cliente_list"),
    path("clientes/create/", cliente.ClienteCreate.as_view(), name="cliente_create"),
    path("servicios/", servicio.ServicioList.as_view(), name="servicios"),
    path("servicios/create/", servicio.ServicioCreate.as_view(), name="servicio_create"),
    path("pedidos/", pedido.PedidoList.as_view(), name="pedidos"),
    path("pedidos/create/", pedido.PedidoCreate.as_view(), name="pedido_create"),
    path(
        "clientes/detail/<int:pk>/",
        cliente.ClienteDetail.as_view(),
        name="cliente_detail",
    ),
    path(
        "clientes/update/<int:pk>/",
        cliente.ClienteUpdate.as_view(),
        name="cliente_update",
    ),
    path(
        "clientes/delete/<int:pk>/",
        cliente.ClienteDelete.as_view(),
        name="cliente_delete",
    ),
    path(
        "servicios/detail/<int:pk>/",
        servicio.ServicioDetail.as_view(),
        name="servicio_detail",
    ),
    path(
        "servicios/update/<int:pk>/",
        servicio.ServicioUpdate.as_view(),
        name="servicio_update",
    ),
    path(
        "servicios/delete/<int:pk>/",
        servicio.ServicioDelete.as_view(),
        name="servicio_delete",
    ),
    path(
        "pedidos/detail/<int:pk>/",
        pedido.PedidoDetail.as_view(),
        name="pedido_detail",
    ),
    path(
        "pedidos/update/<int:pk>/",
        pedido.PedidoUpdate.as_view(),
        name="pedido_update",
    ),
    path(
        "pedidos/delete/<int:pk>/",
        pedido.PedidoDelete.as_view(),
        name="pedido_delete",
    ),
]
