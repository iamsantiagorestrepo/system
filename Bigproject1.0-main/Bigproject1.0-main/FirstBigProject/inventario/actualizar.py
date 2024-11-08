from .utils import cargar_inventario, guardar_inventario



def actualizar_producto(archivo):
    """Permite al usuario actualizar la cantidad y/o precio de un producto existente."""
    inventario = cargar_inventario(archivo)

    if not inventario:
        print("El inventario está vacío.")
        return

    print("Productos en el inventario:")
    for producto in inventario:
        print(f"- {producto} (Cantidad: {inventario[producto]['cantidad']}, Precio: {inventario[producto]['precio']})")

    nombre = input("Ingrese el nombre del producto que desea actualizar: ")

    if nombre in inventario:
        actualizar_cantidad = input(f"¿Desea actualizar la cantidad de {nombre}? (s/n): ").lower()
        if actualizar_cantidad == 's':
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {nombre}: "))
            inventario[nombre]['cantidad'] = nueva_cantidad

        actualizar_precio = input(f"¿Desea actualizar el precio de {nombre}? (s/n): ").lower()
        if actualizar_precio == 's':
            nuevo_precio = float(input(f"Ingrese el nuevo precio de {nombre}: "))
            inventario[nombre]['precio'] = nuevo_precio

        guardar_inventario(archivo, inventario)
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")