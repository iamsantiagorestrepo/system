def invertir_lista(lista):
    lista_invertida = []  # Inicializa una nueva lista vacía
    for elemento in reversed(lista):  # Recorre la lista original en orden inverso
        lista_invertida.append(elemento)  # Agrega cada elemento a la nueva lista
    return lista_invertida

# Ejemplo de uso
lista_original = [1, 2, 3, 4, 5]
resultado = invertir_lista(lista_original)
print("Lista invertida:", resultado)  # Debe imprimir [5, 4, 3, 2, 1]
