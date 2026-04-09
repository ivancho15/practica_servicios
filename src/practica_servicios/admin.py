from django.contrib import admin

from practica_servicios import models

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido_cliente", "nombre_cliente", "celular_cliente")
    search_fields = ("apellido_cliente", "nombre_cliente", "celular_cliente")
    ordering = ("apellido_cliente", "nombre_cliente")

@admin.register(models.Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre_servicio", "precio_servicio","disponible_servicio")
    search_fields = ("nombre_servicio",)
    list_filter = ("disponible_servicio",)
    ordering = ("nombre_servicio", "precio_servicio","disponible_servicio")


@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "servicio", "fecha_solicitud_servicio", "estado_pedido")
    list_filter =("estado_pedido", "fecha_solicitud_servicio")
    search_fields = ("cliente__nombre_cliente", "servicio__nombre_servicio")
    ordering = ("-fecha_solicitud_servicio",)
    date_hierarchy = "fecha_solicitud_servicio"