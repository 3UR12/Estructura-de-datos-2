class Nodo:# Nodo para la lista enlazada
    def __init__(self, producto):# constructor que recibe un producto
        self.producto = producto# asigna el producto al nodo
        self.siguiente = None # inicializa el siguiente nodo como None

# Lista enlazada simple
class ListaEnlazada:# Clase para la lista enlazada
    def __init__(self):
        self.cabeza = None# inicializa la cabeza de la lista como None

    def agregar(self, producto):# método para agregar un producto a la lista
        nuevo = Nodo(producto) # crea un nuevo nodo con el producto
        nuevo.siguiente = self.cabeza # el siguiente del nuevo nodo apunta a la cabeza actual
        self.cabeza = nuevo # la cabeza ahora es el nuevo nodo
        print("Producto agregado.") 

    def eliminar(self, codigo):# método para eliminar un producto por código
        actual = self.cabeza# comienza desde la cabeza
        anterior = None
        while actual:# recorre la lista
            if actual.producto["codigo"] == codigo:# si el código del producto coincide
                if anterior:# si hay un nodo anterior
                    anterior.siguiente = actual.siguiente# el siguiente del nodo anterior apunta al siguiente del nodo actual
                else:
                    self.cabeza = actual.siguiente# si no hay nodo anterior, la cabeza ahora es el siguiente del nodo actual
                print("Producto eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
        print("Producto no encontrado.")

    def buscar(self, codigo):# método para buscar un producto por código
        actual = self.cabeza
        while actual:
            if actual.producto["codigo"] == codigo:
                print(f"Producto encontrado: {actual.producto}")
                return
            actual = actual.siguiente
        print("Producto no encontrado.")

    def mostrar(self):# método para mostrar todos los productos en la lista
        actual = self.cabeza
        if not actual:
            print("No hay productos.")
            return
        print("\nLista de productos:")
        while actual:
            p = actual.producto
            print(f"Nombre: {p['nombre']}, Código: {p['codigo']}, Cantidad: {p['cantidad']}, Precio: ${p['precio']:.2f}")
            actual = actual.siguiente

def menu():
    inventario = ListaEnlazada()

    while True:
        print("\n--- Menú de lista enlazada ---")
        print("1. Agregar producto")
        print("2. Eliminar producto por código")
        print("3. Buscar producto por código")
        print("4. Mostrar productos")
        print("0. Salir")
        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            codigo = int(input("Código: "))
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = {"nombre": nombre, "codigo": codigo, "cantidad": cantidad, "precio": precio}
            inventario.agregar(producto)
        elif op == "2":
            codigo = int(input("Código del producto a eliminar: "))
            inventario.eliminar(codigo)
        elif op == "3":
            codigo = int(input("Código a buscar: "))
            inventario.buscar(codigo)
        elif op == "4":
            inventario.mostrar()
        elif op == "0":
            break
        else:
            print("Opción no válida.")

menu()
