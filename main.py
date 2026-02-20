from cliente import Cliente
from cliente_frecuente import ClienteFrecuente
from venta import Venta
from gestion_clientes import registrar_cliente, buscar_cliente, listar_clientes
from persistencia import guardar_clientes, cargar_clientes

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*40)
    print("1. Registrar nuevo cliente")
    print("2. Registrar cliente frecuente")
    print("3. Buscar cliente")
    print("4. Listar todos los clientes")
    print("5. Registrar venta")
    print("6. Guardar y salir")
    print("="*40)

def registrar_cliente_frecuente(lista_clientes):
    """Registra un cliente frecuente pidiendo datos adicionales."""
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    descuento = float(input("Descuento (0.0 - 1.0, ej: 0.10 para 10%): "))
    
    cliente = ClienteFrecuente(nombre, edad, descuento)
    lista_clientes.append(cliente)
    print(f"✅ Cliente frecuente '{nombre}' registrado con {descuento*100}% de descuento")

def registrar_venta_a_cliente(lista_clientes):
    """Registra una venta para un cliente existente."""
    nombre = input("Nombre del cliente: ")
    cliente = buscar_cliente(lista_clientes, nombre)
    
    if not cliente:
        print("❌ Cliente no encontrado")
        return
    
    print(f"\n📝 Registrando venta para: {cliente.nombre}")
    producto = input("Producto: ")
    subtotal = float(input("Subtotal: $"))
    iva = float(input("IVA: $"))
    total = subtotal + iva
    
    venta = Venta(producto, subtotal, iva, total)
    cliente.agregar_venta(venta)
    
    print(f"✅ Venta de ${total:.2f} registrada")
    
    if isinstance(cliente, ClienteFrecuente):
        print(f"🎯 Puntos acumulados: {cliente.puntos}")

def main():
    """Función principal del programa."""
    print("🔄 Cargando datos...")
    clientes = cargar_clientes()
    print(f"✅ {len(clientes)} cliente(s) cargado(s)")
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            registrar_cliente(clientes)
        
        elif opcion == "2":
            registrar_cliente_frecuente(clientes)
        
        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            cliente = buscar_cliente(clientes, nombre)
            if cliente:
                print("\n✅ Cliente encontrado:")
                cliente.mostrar_info()
            else:
                print("❌ Cliente no encontrado")
        
        elif opcion == "4":
            print("\n📋 LISTA DE CLIENTES:")
            listar_clientes(clientes)
        
        elif opcion == "5":
            registrar_venta_a_cliente(clientes)
        
        elif opcion == "6":
            print("\n💾 Guardando datos...")
            guardar_clientes(clientes)
            print("✅ Datos guardados exitosamente")
            print("👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()