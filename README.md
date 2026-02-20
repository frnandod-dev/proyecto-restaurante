# Sistema de Gestion de Restaurante 

Gestiona clientes de un restaurante permitiendo registrar, guardar y adminitrar a clientes y ventas.

# Descripcion
Los restaurantes necesitan poder gestionar a los clientes con eficiencia y fluidez y este sisitema facilita y permite hacerlo facilmente.

Permite a los restuarantes registrar, guardar y administrar a los clientes y su ClienteFrecuente y su informacion. Y gestiona los pedidos y ventas hechas.

Los clientes frecuentes reciben un acumulado de puntos por cada compra. Calculado por el descuento designado al registrar la venta. 

# Características

-  Gestion de Clientes: Registro, busqueda y listado de clientes.
-  Clientes frecuentes con Descuento: Clientes con beneficios adicionales.
-  Sistema de puntos: Acumulado por descuentos en venta.
-  Historial completo: Guarda el registro comlpleta de ventas del cliente.
-  Registro de ventas: Asigna la venta al cliente.
-  Búsqueda de Clientes: Localiza el nombre por nombre.
-  Persistencia JSON: Guarda y carga automaticamente en formato JSON.

# Instalacion
- main.py

# Requisitos 
- Python 3.2

# Pasos 
1. Clona o descarga el proyecto 
2. Asegurate de tener la carpeta 'datos/' creada:
'''bash
   mkdir datos
'''
3. Ejecuta el programa:
''' bash
    python main.py
''' 
# Uso

### Ejecutar el programa
```bash
python main.py
```

### Menú principal

El sistema presenta las siguientes opciones:

**1. Registrar nuevo cliente**  
Crea un registro de cliente normal solicitando nombre y edad.

**2. Registrar cliente frecuente**
Crea un registro de cliente con beneficios, solicitando nombre, edad y porcentaje de descuento (0.0 - 1.0). Acumula puntos automáticamente en cada compra.

**3. Buscar cliente**  
Busca un cliente por nombre en el registro. Si lo encuentra, muestra toda su información incluyendo historial de ventas.

**4. Listar todos los clientes**  
Muestra el registro completo de todos los clientes con su información y estadísticas.

**5. Registrar venta**  
Asocia una nueva venta a un cliente existente. Solicita producto, subtotal e IVA. Calcula puntos automáticamente para clientes frecuentes.

**6. Guardar y salir**  
Guarda todos los cambios en formato JSON y cierra el programa. Los datos se cargan automáticamente al iniciar nuevamente.

### Ejemplo de flujo
```bash
# 1. Iniciar programa
python main.py

# 2. Registrar cliente frecuente
Opción: 2
Nombre: Ana García
Edad: 28
Descuento: 0.10

# 3. Registrar venta
Opción: 5
Cliente: Ana García
Producto: Tacos al pastor
Subtotal: 100
IVA: 16
# Sistema calcula: Total $116, Puntos: +10

# 4. Guardar y salir
Opción: 6
```

# Estructura del Proyecto
```
Proyecto_Restaurante/
│
├── cliente.py                  # Clase Cliente (cliente normal)
├── cliente_frecuente.py        # Clase ClienteFrecuente (hereda de Cliente)
├── venta.py                    # Clase Venta (registro de transacciones)
├── gestion_clientes.py         # Funciones para gestionar clientes
├── persistencia.py             # Guardado y carga de datos en JSON
├── main.py                     # Programa principal con menú interactivo
│
└── datos/
    └── clientes.json           # Archivo de persistencia (generado automáticamente)
```

### Descripción de módulos

**`cliente.py`**  
Define la clase base `Cliente` con atributos nombre, edad y lista de ventas. Incluye métodos para agregar ventas, calcular total consumido y mostrar información.

**`cliente_frecuente.py`**  
Extiende `Cliente` agregando sistema de descuentos y acumulación de puntos. Cada compra genera puntos basados en el total con descuento aplicado.

**`venta.py`**  
Representa una transacción individual con producto, subtotal, IVA y total. Incluye serialización a JSON.

**`gestion_clientes.py`**  
Funciones utilitarias: `registrar_cliente()`, `buscar_cliente()`, y `listar_clientes()`.

**`persistencia.py`**  
Maneja el guardado y carga de clientes en formato JSON. Crea automáticamente el directorio `datos/` si no existe.

**`main.py`**  
Interfaz de usuario con menú interactivo. Coordina todos los módulos y gestiona el flujo del programa.

## Tecnologías

- **Python 3.10** - Lenguaje de programación
- **JSON** - Formato de persistencia de datos
- **Módulos estándar de Python:**
  - `json` - Serialización de datos
  - `os` - Gestión de archivos y directorios

  ## 👤 Autor

**Fernando Hernandez Rodriguez** - Desarrollador Backend en formación

- 📧 Email: fr.nando.d@gmail.com
- 💼 LinkedIn: www.linkedin.com/in/fernando-hernandez-2589a817a
- 🐙 GitHub: frnandod-dev
---

*Proyecto desarrollado como parte del aprendizaje de Python y programación orientada a objetos.*
