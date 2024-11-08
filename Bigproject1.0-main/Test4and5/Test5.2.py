# Pedir al usuario una lista de palabras separadas por comas
entrada_palabras = input("Introduce una lista de palabras separadas por comas: ")

# Crear una lista de palabras, eliminando espacios adicionales
palabras = [palabra.strip() for palabra in entrada_palabras.split(",")]

# Pedir al usuario una letra para filtrar las palabras
letra = input("Introduce una letra: ").lower()

# Imprimir las palabras que comienzan con la letra especificada
print(f"\nPalabras que comienzan con '{letra}':")
for palabra in palabras:
    if palabra.lower().startswith(letra):
        print(palabra)
