from collections import deque

# Cola de atención para clientes
cola_de_clientes = deque()

lista_de_productos = [# Lista de productos con sus códigos y nombres
    {"codigo": 101, "nombre": "Sal"},
    {"codigo": 102, "nombre": "Azúcar"},
    {"codigo": 103, "nombre": "Arroz"},
    {"codigo": 104, "nombre": "Harina"},
    {"codigo": 105, "nombre": "Aceite"},
    {"codigo": 106, "nombre": "Leche"},
]

# Mostrar los productos disponibles
def mostrar_productos():
    print("\nProductos disponibles:")
    for producto in lista_de_productos:
        print(f"Código: {producto['codigo']} - Nombre: {producto['nombre']}")#

# Agregar cliente a la cola
def agregar_cliente_a_cola():
    nombre_cliente = input("Nombre del cliente: ")
    mostrar_productos()
    codigos_ingresados = input("Ingresar los códigos de productos separados por coma, (101,104): ")
    
    lista_codigos = [
        int(codigo.strip()) #.strip() elimina espacios en blanco
        for codigo in codigos_ingresados.split(",") #. split() divide la cadena en una lista
        if codigo.strip().isdigit()#.isdigit() verifica si es un número
    ]
    
    nuevo_cliente = {# Diccionario que representa al cliente
        "nombre": nombre_cliente,
        "productos_solicitados": lista_codigos
    }
    
    cola_de_clientes.append(nuevo_cliente)#.append() agrega el cliente al final de la cola
    print("Cliente agregado a la cola.")

# Atender al siguiente cliente en la cola
def atender_siguiente_cliente():
    if cola_de_clientes:
        cliente_atendido = cola_de_clientes.popleft()#.popleft() elimina y devuelve el primer cliente de la cola
        print(f"\nAtendiendo a: {cliente_atendido['nombre']}")
        
        if cliente_atendido['productos_solicitados']:
            print("Productos solicitados:")
            for codigo in cliente_atendido['productos_solicitados']:
                nombre_producto = next(#next() obtiene el primer elemento del generador
                    (producto['nombre'] for producto in lista_de_productos if producto['codigo'] == codigo),
                    "Producto no encontrado"
                )
                print(f"- Código: {codigo}, Nombre: {nombre_producto}")
        else:
            print("No solicitó productos.")
    else:
        print("No hay clientes en la cola.")

# Mostrar todos los clientes en espera
def mostrar_clientes_en_espera():
    if not cola_de_clientes:
        print("No hay clientes en espera.")
    else:
        print("\nClientes en la cola:")
        for cliente in cola_de_clientes:
            print(f"- {cliente['nombre']} (productos solicitados: {len(cliente['productos_solicitados'])})")

# Menú 
def menu_de_colas():
    while True:
        print("\n--- Menu de cola ---")
        print("1. Agregar cliente")
        print("2. Atender cliente")
        print("3. Ver clientes en espera")
        print("4. Ver productos disponibles")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente_a_cola()
        elif opcion == "2":
            atender_siguiente_cliente()
        elif opcion == "3":
            mostrar_clientes_en_espera()
        elif opcion == "4":
            mostrar_productos()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu_de_colas()
