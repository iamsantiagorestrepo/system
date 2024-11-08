# Pedimos al usuario que ingrese una palabra o frase
frase = input("Ingresa una palabra o frase: ").lower()

# Inicializamos contadores para cada vocal
a = e = i = o = u = 0

# Ciclo for para contar las vocales
for letra in frase:
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1

# Mostramos el conteo de cada vocal
print(f"La vocal 'a' aparece {a} veces.")
print(f"La vocal 'e' aparece {e} veces.")
print(f"La vocal 'i' aparece {i} veces.")
print(f"La vocal 'o' aparece {o} veces.")
print(f"La vocal 'u' aparece {u} veces.")