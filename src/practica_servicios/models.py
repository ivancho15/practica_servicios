from django.db import models

class Cliente(models.Model):
    id_cliente = models.UUIDField(editable=False, unique=True, primary_key=True)
    nombre_cliente = models.CharField(max_length=45)
    apellido_cliente = models.CharField(max_length=45)
    celular_cliente = models.CharField(max_length=20)
    domicilio_cliente = models.TextField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre_cliente.capitalize()} {self.apellido_cliente.capitalize()}"
    
    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=50)
    decripcion_servicio = models.TextField(max_length=150)
    precio_servicio = models.DecimalField(max_digits=6, decimal_places=2)
    dispoible_servico = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.nombre_servicio.capitalize()}: {self.decripcion_servicio.capitalize()}. costo: {self.precio_servicio}"
    
    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"


class Pedido(models.Model):
    class EstadoPedido(models.TextChoices):
        PENDIENTE = 'PE', ('Pendiente')
        EN_PROGRESO = 'EP', ('En progreso')
        COMPLETADO = 'CO', ('Completado')
    
    id_pedido = models.UUIDField(editable=False, unique=True, primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=False)
    descripcion_pedido = models.TextField(max_length=100)
    fecha_solicitud_servicio = models.DateField(null=False, blank=False)
    fecha_finalizacion_Servicio = models.DateField(null=False, blank=False)
    estado_pedido = models.CharField(max_length=2, choices=EstadoPedido.choices, default=EstadoPedido.PENDIENTE)

    def __str__(self) -> str:
        return f"{self.id_pedido}: {self.estado_pedido}"
    
