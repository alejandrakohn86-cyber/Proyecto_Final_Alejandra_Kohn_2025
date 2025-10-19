import uuid

class Cliente:
    tipo = "Consumidor Final" # Atributo de clase

    def __init__(self, nombre, apellido, documento, domicilio, telefono): 
        self.id = uuid.uuid4()           
        self.nombre = nombre             # Atributos públicos
        self.apellido = apellido
        self.__documento = documento     # Atributos privados
        self.__domicilio = domicilio
        self.__telefono = telefono

    def __str__(self):
        return f"ID: {self.id} - Cliente: {self.nombre} {self.apellido} - Tipo: {self.tipo}"    

    # Getters
    def get_documento(self):
        return f"DNI: {self.__documento}"

    def get_domicilio(self):
        return f"Domicilio: {self.__domicilio}"    

    def get_telefono(self):
        return f"Teléfono: {self.__telefono}"    

    # Setters
    def set_documento(self, documento):
        self.__documento = documento
    
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio    
    
    def set_telefono(self, telefono):
        self.__telefono = telefono    

    # Métodos de negocio
    def comprar(self, producto, cantidad=1):
        if not producto.descontar_stock(cantidad):
            print(f"No hay suficiente stock de {producto.nombre}")
            return False
            
        print(f"{self.nombre} {self.apellido} compró {cantidad} unidad(es) de {producto.nombre}")
        print(f"Stock restante: {producto._Producto__stock} unidades")
        return True
