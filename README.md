````markdown
# Proyecto: Inventario con Estructuras de Datos

Este proyecto es una aplicación que permite administrar un inventario usando diferentes estructuras de datos en Python. Fue desarrollado como práctica para entender cómo funcionan los arreglos, listas enlazadas, pilas, colas y árboles binarios de búsqueda (ABB).

Cada estructura tiene su propio archivo `.py` y cumple una función específica en el sistema de inventario.

## Archivos del proyecto

| Archivo                     | Función principal                                                       |
|-----------------------------|-------------------------------------------------------------------------|
| `arreglos.py`               | Almacena productos y permite ordenarlos por nombre o precio.            |
| `listas_enlazadas.py`       | Permite agregar, eliminar y buscar productos dinámicamente.             |
| `pilas.py`                  | Guarda un historial de cambios y permite deshacer la última acción.     |
| `colas.py`                  | Simula la atención de clientes en orden de llegada.                     |
| `arbol_binario_busqueda.py` | Inserta y busca productos de forma eficiente usando un árbol binario.   |

---

## 1. Arreglos (`arreglos.py`)

Usa una lista de diccionarios para guardar productos con estos datos:

- `nombre`
- `codigo`
- `cantidad`
- `precio`

### Funciones:

- `mostrar_productos()`: muestra los productos.
- `ordenar_por_nombre()`: ordena por nombre alfabéticamente.
- `ordenar_por_precio()`: ordena de menor a mayor precio.
- `menu()`: menú interactivo.

### Ejecutar:

```bash
python arreglos.py
````

---

## 2. Listas Enlazadas (`listas_enlazadas.py`)

Permite manejar productos de forma dinámica. Cada nodo de la lista guarda un producto.

### Funciones:

* `agregar(producto)`: añade un producto.
* `eliminar(codigo)`: elimina por código.
* `buscar(codigo)`: busca un producto.
* `mostrar()`: muestra todos los productos.
* `menu()`: menú interactivo.

### Ejecutar:

```bash
python listas_enlazadas.py
```

---

## 3. Pilas (`pilas.py`)

Usa una pila para llevar un historial de las últimas 10 operaciones: agregar, eliminar o editar productos. Permite deshacer la última.

### Funciones:

* `registrar_operacion(accion, producto)`: guarda en el historial.
* `deshacer()`: revierte la última acción.
* `agregar_producto()`, `eliminar_producto()`, `editar_producto()`, `mostrar_productos()`: operaciones básicas del inventario.
* `menu()`: menú interactivo.

### Ejecutar:

```bash
python pilas.py
```

---

## 4. Colas (`colas.py`)

Simula una fila de clientes que hacen pedidos. Cada cliente indica qué productos quiere por su código.

### Funciones:

* `agregar_cliente_a_cola()`: agrega un cliente con su pedido.
* `atender_siguiente_cliente()`: atiende al primero en la cola.
* `mostrar_clientes_en_espera()`: muestra quiénes están esperando.
* `mostrar_productos()`: lista de productos disponibles.
* `menu_de_colas()`: menú interactivo.

### Ejecutar:

```bash
python colas.py
```

---

## 5. Árbol Binario de Búsqueda (ABB) (`arbol_binario_busqueda.py`)

Guarda los productos en un árbol binario ordenado por código para facilitar búsquedas rápidas.

### Funciones:

* `insertar_producto_en_arbol(raiz, producto)`: inserta un producto.
* `buscar_producto_en_arbol(raiz, codigo)`: busca por código.
* `recorrido_inorden(raiz)`: muestra los productos ordenados.
* `menu_arbol_binario()`: menú interactivo.

### Ejecutar:

```bash
python arbol_binario_busqueda.py
```

---

## Requisitos

* Python 3.x
* No se necesita instalar librerías externas (solo se usa `collections` que ya viene con Python).

---

## Créditos

Este proyecto fue creado como práctica de estructuras de datos en Python para representar un sistema de inventario simple, usando algoritmos básicos y menús interactivos por consola.

