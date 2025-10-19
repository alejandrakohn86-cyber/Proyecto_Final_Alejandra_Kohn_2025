from .cliente import Cliente

class ClienteCorporativo(Cliente): 
    tipo = "Persona Jurídica" # Atributo de clase

    def __init__(self, nombre, apellido, documento, domicilio, telefono, cuit, razon_social, nombre_fantasia):
        # Hereda de Cliente
        super().__init__(nombre, apellido, documento, domicilio, telefono) 
        self.__cuit = cuit      # Atributo privado
        self.razon_social = razon_social     # Atributos públicos
        self.nombre_fantasia = nombre_fantasia
        
    def __str__(self):
        return (f"ID: {self.id} - Cliente Corporativo: {self.razon_social} \n"
                f"Nombre Fantasía: {self.nombre_fantasia} | CUIT: {self.__cuit} | Tipo: {self.tipo} \n"
                f"Apoderado Legal: {self.nombre} {self.apellido}")

    # Getters
    def get_cuit(self):
        return f"CUIT: {self.__cuit}"

    # Setters
    def set_cuit(self, cuit):
        self.__cuit = cuit
        