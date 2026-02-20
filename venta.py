class Venta:
    """
        Representa una venta realizada a un cliente.
    
        Almacena la información completa de una transacción incluyendo
        el producto vendido, su precio base (subtotal), el impuesto
        aplicado (IVA) y el monto total cobrado.
    
        Attributes:
            producto (str): Nombre del producto vendido
            subtotal (float): Precio base sin impuestos
            iva (float): Impuesto al Valor Agregado calculado
            total (float): Monto total (subtotal + iva)
    """
    def __init__(self, producto, subtotal, iva, total):
        self.producto = producto
        self.subtotal = subtotal
        self.iva = iva 
        self.total = total
    
    def to_dict(self):
        """
        Convierte el objeto Venta en diccionario para JSON
        Serializa la informacion de la venta y de sus impuestos aplicado
        y el total.

        Returns:
            dict: Diccionario con informacion de la venta
            - producto(str): nombre del producto 
            - subtotal(float): precio base sin impuesto 
            - iva(float): impuesto agragado al subtotal
            - total(float): Monto total (subtotal + iva)
        """
        return {
            "producto": self.producto,
            "subtotal": self.subtotal,
            "iva": self.iva,
            "total": self.total
        }

        