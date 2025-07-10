# 📦 Proyecto: Inventario con Estructuras de Datos

Este proyecto es una aplicación en Python que permite administrar un inventario utilizando distintas estructuras de datos. Cada archivo contiene una estructura distinta (arreglos, listas enlazadas, pilas, colas y árboles binarios de búsqueda), con menús interactivos para probarlas.

---

## 📁 Archivos del Proyecto

| Archivo                     | Descripción                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| `arreglos.py`               | Guarda productos y permite ordenarlos por nombre o precio.             |
| `listas_enlazadas.py`       | Permite agregar, eliminar y buscar productos dinámicamente.            |
| `pilas.py`                  | Lleva un historial de operaciones (agregar, eliminar, editar).         |
| `colas.py`                  | Simula la atención a clientes en orden de llegada (FIFO).              |
| `arbol_binario_busqueda.py` | Inserta y busca productos usando un árbol binario ordenado por código. |

---

## 🗂️ 1. Arreglos (`arreglos.py`)

Se utiliza una lista de diccionarios para almacenar productos con los siguientes atributos:

* `nombre`
* `codigo`
* `cantidad`
* `precio`

### Funciones disponibles

* `mostrar_productos()`
* `ordenar_por_nombre()`
* `ordenar_por_precio()`
* `menu()`

### Ejecutar

```bash
python arreglos.py
```

---

## 🔗 2. Listas Enlazadas (`listas_enlazadas.py`)

Permite administrar el inventario dinámicamente mediante una lista enlazada simple.

### Funciones disponibles

* `agregar(producto)`
* `eliminar(codigo)`
* `buscar(codigo)`
* `mostrar()`
* `menu()`

### Ejecutar

```bash
python listas_enlazadas.py
```

---

## 🧱 3. Pilas (`pilas.py`)

Lleva un historial de las últimas 10 operaciones y permite deshacer la última acción.

### Funciones disponibles

* `registrar_operacion(accion, producto)`
* `deshacer()`
* `agregar_producto()`
* `eliminar_producto()`
* `editar_producto()`
* `mostrar_productos()`
* `menu()`

### Ejecutar

```bash
python pilas.py
```

---

## ⏳ 4. Colas (`colas.py`)

Simula una fila de atención a clientes que piden productos. Se atienden en orden de llegada (FIFO).

### Funciones disponibles

* `agregar_cliente_a_cola()`
* `atender_siguiente_cliente()`
* `mostrar_clientes_en_espera()`
* `mostrar_productos()`
* `menu_de_colas()`

### Ejecutar

```bash
python colas.py
```

---

## 🌳 5. Árbol Binario de Búsqueda (`arbol_binario_busqueda.py`)

Permite insertar, buscar y mostrar productos ordenados por código mediante un ABB.

### Funciones disponibles

* `insertar_producto_en_arbol(raiz, producto)`
* `buscar_producto_en_arbol(raiz, codigo)`
* `recorrido_inorden(raiz)`
* `menu_arbol_binario()`

### Ejecutar

```bash
python arbol_binario_busqueda.py
```

---

## ✅ Requisitos

* Python 3.x
* No requiere librerías externas (solo `collections`, incluida en Python)

---

## 👨‍💻 Créditos

Desarrollado como ejercicio de estructuras de datos en Python para simular la gestión de un inventario.
