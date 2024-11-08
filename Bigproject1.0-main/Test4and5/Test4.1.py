def eliminar_duplicados(lista):
    vistos = set()
    nueva_lista = []
    for x in lista:
        if x not in vistos:
            nueva_lista.append(x)
            vistos.add(x)
    return nueva_lista

# Ejemplo de uso
lista_original = [1, 2, 2, 3, 4, 4, 5, 5, 6]
resultado = eliminar_duplicados(lista_original)
print("Lista sin duplicados:", resultado)  # Debe imprimir [1, 2, 3, 4, 5, 6]
