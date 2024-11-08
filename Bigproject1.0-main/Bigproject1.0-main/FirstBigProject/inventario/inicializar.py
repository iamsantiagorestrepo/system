import json
import os

def inicializar_inventario(archivo):
    """Crea un archivo JSON con datos de inventario iniciales si no existe."""
    if not os.path.exists(archivo):
        inventario_inicial = {
            "Producto A": {"cantidad": 10, "precio": 5.99},
            "Producto B": {"cantidad": 20, "precio": 2.49},
            "Producto C": {"cantidad": 15, "precio": 3.75}
        }

        with open(archivo, 'w') as f:
            json.dump(inventario_inicial, f, indent=4)
        print(f"El archivo '{archivo}' ha sido creado con datos iniciales.")
    else:
        print(f"El archivo '{archivo}' ya existe. No se han creado datos iniciales.")

if __name__ == "__main__":
    archivo_inventario = 'datos/inventario.json'  # Ruta al archivo de inventario
    inicializar_inventario(archivo_inventario)
