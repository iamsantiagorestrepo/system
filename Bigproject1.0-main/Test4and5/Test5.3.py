# Pedir al usuario una lista de números separados por comas
entrada_numeros = input("Introduce una lista de números separados por comas: ")

# Convertir la entrada en una lista de números enteros
numeros = [int(numero.strip()) for numero in entrada_numeros.split(",")]

# Inicializar la variable para la suma de números pares
suma_pares = 0

# Recorrer la lista y sumar los números pares
for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero

# Imprimir la suma de los números pares
print(f"\nLa suma de los números pares es: {suma_pares}")
