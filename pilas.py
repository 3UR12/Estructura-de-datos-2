# Lista de productos
productos = []

# Pila para el historial (máximo 10 elementos)
historial = []


def registrar_operacion(accion, producto):# función para registrar operaciones
    historial.append((accion, producto.copy()))# copia el producto con el metodo copy()
    if len(historial) > 10:# verifica si el historial supera los 10 elementos
        print("Historial lleno, eliminando la ultima operacion.")
        historial.pop(0)# elimina el primer elemento del historial si es necesario

def deshacer():# función para deshacer la última operación
    if not historial:# verifica si el historial está vacío
        print("No hay operaciones para deshacer.")
        return
    accion, producto = historial.pop()# obtiene la última operación del historial
    
    if accion == "agregar":# verifica si la acción es agregar
        for p in productos:
            if p["codigo"] == producto["codigo"]:
                productos.remove(p)# elimina el producto del arreglo
                print("Se deshizo la adición del producto.")
                return# sale de la función
    elif accion == "eliminar":# verifica si la acción es eliminar
        productos.append(producto)# agrega el producto de nuevo al arreglo
        print("Se deshizo la eliminación del producto.")
    elif accion == "editar":# verifica si la acción es editar
        for i, p in enumerate(productos):# recorre el arreglo de productos
            if p["codigo"] == producto["codigo"]:# verifica si el código coincide
                productos[i] = producto
                print("Se deshizo la edición del producto.")
                return

def agregar_producto():# función para agregar un producto
    nombre = input("Nombre: ")
    codigo = int(input("Código: "))
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    producto = {"nombre": nombre, "codigo": codigo, "cantidad": cantidad, "precio": precio}
    productos.append(producto)# agrega el producto al arreglo
    registrar_operacion("agregar", producto)# registra la operación de adición
    print("Producto agregado.")

def eliminar_producto():# función para eliminar un producto
    codigo = int(input("Código del producto a eliminar: "))#pide el codigo
    for p in productos:
        if p["codigo"] == codigo:#verifica si el código en el arreglo coincide
            registrar_operacion("eliminar", p)# registra la operación de eliminación
            productos.remove(p)# elimina el producto del arreglo
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

def editar_producto():# función para editar un producto
    codigo = int(input("Código del producto a editar: "))# solicita el código del producto a editar
    for p in productos:
        if p["codigo"] == codigo:# verifica si el código coincide con algún producto
            registrar_operacion("editar", p.copy())# registra la operación de edición
            p["nombre"] = input(f"Nuevo nombre ({p['nombre']}): ") or p["nombre"]#comienza a editar el producto
            p["cantidad"] = int(input(f"Nueva cantidad ({p['cantidad']}): ") or p["cantidad"])
            p["precio"] = float(input(f"Nuevo precio ({p['precio']}): ") or p["precio"])
            print("Producto editado.")
            return
    print("Producto no encontrado.")

def mostrar_productos():# función para mostrar los productos
    if not productos:
        print("No hay productos.")
        return
    for p in productos:
        print(f"Nombre: {p['nombre']}, Código: {p['codigo']}, Cantidad: {p['cantidad']}, Precio: ${p['precio']:.2f}")#2f para formatear el precio a dos decimales y f para indicar que es un float

def menu():
    while True:
        print("\n--- menu para pilas ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Editar producto")
        print("4. Ver productos")
        print("5. Deshacer última operación")
        print("0. Salir")
        op = input("Opción: ")

        if op == "1":#el metodo op es una variable que almacena la opcion del usuario
            agregar_producto()
        elif op == "2":
            eliminar_producto()
        elif op == "3":
            editar_producto()
        elif op == "4":
            mostrar_productos()
        elif op == "5":
            deshacer()
        elif op == "0":
            break
        else:
            print("Opción no válida.")

# Ejecutar
menu()
