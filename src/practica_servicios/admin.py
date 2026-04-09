from django.contrib import admin

from practica_servicios import models

admin.site.register(models.Cliente)
admin.site.register(models.Servicio)
admin.site.register(models.Pedido)


