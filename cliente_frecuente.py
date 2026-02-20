from cliente import Cliente
class ClienteFrecuente(Cliente):
    """
    Cliente con beneficios especiales: descuento y sistema de puntos.
    
    Hereda de Cliente y agrega funcionalidad de descuentos en cada
    compra y acumulación de puntos según el total consumido.
    
    Attributes:
        nombre (str): Nombre del cliente (heredado)
        edad (int): Edad del cliente (heredado)
        ventas (list): Lista de ventas (heredado)
        descuento (float): Porcentaje de descuento (0.0 a 1.0)
        puntos (int): Puntos acumulados (1 punto por cada $10)
    """
    def __init__(self, nombre, edad, descuento):
        super().__init__(nombre, edad)
        self.descuento = descuento
        self.puntos = 0 
    def agregar_venta(self, venta):
        """
        Agregar una venta  al cliente frecuente aplicando su descuento.

        El descuento solo afecta el calculo de puntos,
        no modifica el objeto vente original

        Args: 
            venta: Objeto venta a agregar
        returns:
            Resultado del metodo agregar_venta del padre
        """
        total_con_descuento = venta.total * (1- self.descuento)
        self.puntos += int(total_con_descuento // 10)
        return super().agregar_venta(venta)

    
    def to_dict(self):
        """
        Convierte el objeto ClienteFrecuente a diccionario para JSON.
    
        Serializa toda la información del cliente frecuente incluyendo
        sus atributos específicos (descuento y puntos) y sus ventas.
        El campo 'tipo' permite distinguirlo de clientes normales al
        cargar desde JSON.
    
        Returns:
            dict: Diccionario con toda la información del cliente:
                - tipo (str): "frecuente"
                - nombre (str): Nombre del cliente
                - edad (int): Edad del cliente
                - descuento (float): Porcentaje de descuento
                - puntos (int): Puntos acumulados
                - ventas (list): Lista de diccionarios de ventas
        """ 
        return {
            "tipo": "frecuente",
            "nombre": self.nombre,
            "edad": self.edad,
            "descuento": self.descuento,
            "puntos": self.puntos,
            "ventas": [v.to_dict() for v in self.ventas]
        }