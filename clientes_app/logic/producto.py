import uuid

class Producto:
    CATEGORIA_DEFAULT = 'Sin categoría asignada'  # Atributos de clase
    CATEGORIA_ELECTRONICA = 'Electrónica'
    CATEGORIA_INDUMENTARIA = 'Indumentaria'
    CATEGORIA_ALIMENTOS = 'Alimentos'
    CATEGORIA_HOGAR = 'Hogar'
    
    def __init__(self, nombre, descripcion, precio, stock, codigo_sku=None, categoria=None):          
        self.nombre = nombre             # Atributos públicos
        self.categoria = categoria if categoria else Producto.CATEGORIA_DEFAULT  
        self.descripcion = descripcion
        self.__precio = precio   # Atributos privados
        self.__stock = stock
        self.__codigo_sku = codigo_sku or str(uuid.uuid4())[:8].upper()  
        
    def __str__(self):
        return f"Código SKU: {self.__codigo_sku} - Producto: {self.nombre} - Precio: ${self.__precio} - Categoría: {self.categoria} - Descripción: {self.descripcion}"
        
    # Getters
    def get_precio(self):
        return f"Precio: ${self.__precio}"
    
    def get_stock(self):
        return f"Stock disponible: {self.__stock} unidades"
        
    def get_codigo_sku(self):
        return f"Código SKU: {self.__codigo_sku}"
        
    # Setters
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que cero")

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            raise ValueError("El stock no puede ser negativo")
            
    def set_codigo_sku(self, codigo_sku):
        self.__codigo_sku = codigo_sku
        
    # Métodos adicionales
    def hay_stock(self):
        return self.__stock > 0
        
    def descontar_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False
        
    def aumentar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
            return True
        return False
        
    def vender_a(self, cliente, cantidad=1):
        return cliente.comprar(self, cantidad)