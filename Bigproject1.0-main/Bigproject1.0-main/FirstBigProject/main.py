from inventario.agregar import agregar_producto
from inventario.actualizar import actualizar_producto
from inventario.eliminar import eliminar_producto
from inventario.mostrar import mostrar_inventario
from inventario.inicializar import inicializar_inventario


def menu():
    """Muestra el menú de opciones y ejecuta la opción seleccionada."""
    archivo_inventario = 'datos/inventario.json'

    # Inicializar el inventario al comenzar el programa
    inicializar_inventario(archivo_inventario)

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_producto(archivo_inventario)
        elif opcion == '2':
            actualizar_producto(archivo_inventario)
        elif opcion == '3':
            eliminar_producto(archivo_inventario)
        elif opcion == '4':
            mostrar_inventario(archivo_inventario)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
