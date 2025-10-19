from django.db import models
import uuid
from django.utils import timezone

# Función para generar códigos SKU
def generate_sku():
    return str(uuid.uuid4())[:8].upper()

# Modelo Cliente
class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50, default="Consumidor Final")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} - Tipo: {self.tipo} - Fecha de Registro: {self.fecha_registro.strftime('%d/%m/%Y %H:%M:%S')}"
    
    # Ordenar por apellido y nombre
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido", "nombre"]
    
    # Método comprar
    def comprar(self, producto, cantidad=1):
        if not producto.descontar_stock(cantidad):
            return False

        from clientes_app.models import Compra    

        # Registrar la compra 
        Compra.objects.create(
            cliente=self,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio,
            fecha_compra=timezone.now()
        )
        return True


# Modelo Cliente Corporativo
class ClienteCorporativo(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)
    cuit = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=100)
    nombre_fantasia = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Cliente: {self.razon_social} ({self.nombre_fantasia}) - CUIT: {self.cuit} - Apoderado Legal: {self.cliente.nombre} {self.cliente.apellido} - Fecha de Registro: {self.cliente.fecha_registro.strftime('%d/%m/%Y %H:%M:%S')}"
    
    # Ordenar por razón social
    class Meta:
        verbose_name = "Cliente Corporativo"
        verbose_name_plural = "Clientes Corporativos"
        ordering = ["razon_social"]
    
    # Delegar el método comprar al cliente asociado
    def comprar(self, producto, cantidad=1):
        return self.cliente.comprar(producto, cantidad)


# Modelo Producto
class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('DEFAULT', 'Sin categoría asignada'),
        ('ELECTRONICA', 'Electrónica'),
        ('INDUMENTARIA', 'Indumentaria'),
        ('ALIMENTOS', 'Alimentos'),
        ('HOGAR', 'Hogar'),
    ]
    
    codigo_sku = models.CharField(max_length=20, primary_key=True, default=generate_sku, editable=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='DEFAULT')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Ordenar por nombre
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]
    
    def __str__(self):
        return f"Código SKU: {self.codigo_sku} - Producto: {self.nombre} - Precio: ${self.precio} - Categoría: {self.categoria} - Descripción: {self.descripcion}"
    

    # Métodos de stock y venta
    def hay_stock(self):
        return self.stock > 0
    
    def descontar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            self.save()
            return True
        return False
        
    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            self.save()
            return True
        return False
        
    def vender_a(self, cliente, cantidad=1):
        return cliente.comprar(self, cantidad)

# Modelo Compra
class Compra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='compras')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateTimeField(default=timezone.now)
    
    # Ordenar por fecha de compra
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ["-fecha_compra"]
    
    def __str__(self):
        return f"{self.cliente} compró {self.cantidad} de {self.producto} el {self.fecha_compra.strftime('%d/%m/%Y %H:%M:%S')}"
    
    # Calcula el precio total de la compra
    @property
    def precio_total(self):
        return self.precio_unitario * self.cantidad