productos = [
    {"nombre": "Sal", "codigo": 101, "cantidad": 50, "precio": 1.50},
    {"nombre": "Azucar", "codigo": 102, "cantidad": 30, "precio": 2.00},
    {"nombre": "Arroz", "codigo": 103, "cantidad": 20, "precio": 3.00},
    {"nombre": "Harina", "codigo": 104, "cantidad": 15, "precio": 1.75},
    {"nombre": "Aceite", "codigo": 105, "cantidad": 25, "precio": 4.50},
    {"nombre": "Leche", "codigo": 106, "cantidad": 40, "precio": 1.20}
]

# Mostrar productos
def mostrar_productos():
    try:#try para manejar errores
        print("\nLista de productos:")
        for p in productos:#for para recorrer la lista de productos e imprimir los datos
            print(f"Nombre: {p['nombre']}, Código: {p['codigo']}, Cantidad: {p['cantidad']}, Precio: ${p['precio']:.2f}")
    except Exception as e:
        print(f"Error al mostrar productos: {e}")

# Ordenar por nombre (alfabéticamente)
def ordenar_por_nombre():
    try:
        productos.sort(key=lambda p: p['nombre'])# este metodo ordena la lista de productos por nombre
        print("\nProductos ordenados por nombre.")
    except Exception as e:
        print(f"Error al ordenar productos por nombre: {e}")

# Ordenar por precio
def ordenar_por_precio():
    try:
        productos.sort(key=lambda p: p['precio'])# este metodo ordena la lista de productos por precio
        print("\nProductos ordenados por precio.")
    except Exception as e:
        print(f"Error al ordenar productos por precio: {e}")

# Menú simple para probar
def menu():
    try:#esto puede ser innecesarioo
        while True:
            print("\n--- MENÚ ARREGLO ---")
            print("1. Ver productos")
            print("2. Ordenar por nombre")
            print("3. Ordenar por precio")
            print("0. Salir")
            op = input("Opción: ")

            if op == "1":
                mostrar_productos()
            elif op == "2":
                ordenar_por_nombre()
            elif op == "3":
                ordenar_por_precio()
            elif op == "0":
                break
            else:
                print("Opción no válida.")
    except Exception as e:
        print(f"Error en el menú: {e}")

# Ejecutar
menu()
