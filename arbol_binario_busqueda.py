# Clase que representa un nodo del árbol binario
class NodoDelArbol:
    def __init__(self, producto):
        self.producto = producto# Guarda los datos del producto
        self.subarbol_izquierdo = None #subárbol izquierdo 
        self.subarbol_derecho = None# subárbol derecho


# Función para insertar un nuevo producto en el árbol, ordenado por código
def insertar_producto_en_arbol(raiz, producto_nuevo):
    if raiz is None:# Si el árbol está vacío, creamos un nuevo nodo
        return NodoDelArbol(producto_nuevo)

    # Si el código del nuevo producto es menor, va al subárbol izquierdo
    if producto_nuevo["codigo"] < raiz.producto["codigo"]:
        raiz.subarbol_izquierdo = insertar_producto_en_arbol(raiz.subarbol_izquierdo, producto_nuevo)
    else:
        # Si es mayor o igual, va al subárbol derecho
        raiz.subarbol_derecho = insertar_producto_en_arbol(raiz.subarbol_derecho, producto_nuevo)

    return raiz  # Devuelve la raíz actual para mantener el árbol conectado


# Función para buscar un producto por su código en el árbol
def buscar_producto_en_arbol(raiz, codigo_a_buscar):
    if raiz is None:# si no hay más nodos, el producto no se encuentra
        return None

    # Si el código coincide con el nodo actual, se devuelve el producto
    if codigo_a_buscar == raiz.producto["codigo"]:
        return raiz.producto
    elif codigo_a_buscar < raiz.producto["codigo"]:# Si el código es menor, busca en el subárbol izquierdo
        return buscar_producto_en_arbol(raiz.subarbol_izquierdo, codigo_a_buscar)
    else:
        # Si es mayor, busca en el subárbol derecho
        return buscar_producto_en_arbol(raiz.subarbol_derecho, codigo_a_buscar)

# Función para mostrar todos los productos en inodern
def recorrido_inorden(raiz):
    if raiz is not None:
        # Recorrer primero el subárbol izquierdo
        recorrido_inorden(raiz.subarbol_izquierdo)
        producto = raiz.producto
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")
        #recorre el subárbol derecho
        recorrido_inorden(raiz.subarbol_derecho)


def menu_arbol_binario():
    raiz_del_arbol = None  # Inicializar la raíz del árbol como None

    while True:
        print("\n--- MENÚ ÁRBOL BINARIO DE BÚSQUEDA ---")
        print("1. Insertar producto")
        print("2. Buscar producto por código")
        print("3. Mostrar productos ordenados (inorden)")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Ingreso de datos del nuevo producto
            nombre = input("Nombre del producto: ")
            codigo = int(input("Código del producto: "))
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio por unidad: "))
            
            # Crear diccionario
            producto_nuevo = {
                "nombre": nombre,
                "codigo": codigo,
                "cantidad": cantidad,
                "precio": precio
            }

            # Insertar el producto en el árbol
            raiz_del_arbol = insertar_producto_en_arbol(raiz_del_arbol, producto_nuevo)
            print("Producto insertado en el árbol.")

        elif opcion == "2":
            # Buscar un producto por su código
            codigo_a_buscar = int(input("Ingrese el código del producto a buscar: "))
            resultado = buscar_producto_en_arbol(raiz_del_arbol, codigo_a_buscar)

            # Mostrar resultado
            if resultado:
                print(f"Producto encontrado: {resultado}")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            print("\nProductos ordenados por código:")
            recorrido_inorden(raiz_del_arbol)

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intente nuevamente.")

menu_arbol_binario()
