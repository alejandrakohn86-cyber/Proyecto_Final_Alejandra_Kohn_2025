from django.contrib import admin
from .models import Cliente, ClienteCorporativo, Producto, Compra

# Personalización del panel de administración
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'domicilio', 'telefono', 'tipo', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'documento')
    list_filter = ('tipo', 'fecha_registro')

class ClienteCorporativoAdmin(admin.ModelAdmin):
    list_display = ('razon_social', 'nombre_fantasia', 'cuit', 'get_apoderado')
    search_fields = ('razon_social', 'nombre_fantasia', 'cuit')

    def get_apoderado(self, obj):
        return f"{obj.cliente.nombre} {obj.cliente.apellido}"
    get_apoderado.short_description = 'Apoderado'

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_sku', 'precio', 'stock', 'categoria', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion', 'codigo_sku')
    list_filter = ('categoria', 'fecha_creacion')
    list_editable = ('precio', 'stock')

class CompraAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'precio_unitario', 'precio_total', 'fecha_compra')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'producto__nombre')
    list_filter = ('fecha_compra',)
    date_hierarchy = 'fecha_compra'
    readonly_fields = ('precio_total',)

# Registrar los modelos
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ClienteCorporativo, ClienteCorporativoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Compra, CompraAdmin)
