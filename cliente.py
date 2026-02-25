class Cliente:
    """
Representa un cliente del restaurante.

Gestiona la información personal del cliente y mantiene un registro
de todas sus compras realizadas.

Args:
    nombre (str): Nombre completo del cliente
    edad (int): Edad del cliente en años
    ventas (list): Lista de objetos Venta asociados al cliente
"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.ventas = []
        if self.edad < 1:
            raise ValueError("La edad no puede ser negativa")
    
    
    def agregar_venta(self, venta):
        """
        Agrega la venta al cliente a la lista self.ventas
        Args:
        venta(Venta): Objeto Venta a agregar a la lista.
        """
        self.ventas.append(venta)
    
    def total_consumido(self):
        """
        Calcula el total de dinero consumido por el cliente.
    
        Suma los totales de todas las ventas registradas.
    
        Returns:
            float: Total consumido en pesos
        """
        return sum(v.total for v in self.ventas)
    
    def mostrar_info(self):
        """
        Muestra en consola la información del cliente.
    
        Imprime nombre, edad, cantidad de ventas y total consumido.
        """
        print(f"Cliente: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Ventas: {len(self.ventas)}")
        print(f"Total consumido: ${self.total_consumido(): .2f}")
    
    def listar_ventas(self):
        if not self.ventas:
            print("el cliente no tiene ventas registradas")
            return
        
        print(f"Ventas de {self.nombre}")
        for i, venta in enumerate(self.ventas, start=1):
            print(f"\nVenta {i}")
            print(f"Producto: {venta.producto}")
            print(f"Subtotal: ${venta.subtotal}")
            print(f"IVA: ${venta.iva}")
            print(f"Total: ${venta.total}")
    def to_dict(self):
        return {
            "tipo": "normal",
            "nombre": self.nombre,
            "edad": self.edad,
            "ventas": [v.to_dict() for v in self.ventas]
        }