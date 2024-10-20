import os
os.system("cls")

numeros = []
contador = 0
suma = 0

# Usar un bucle while para obtener 10 números
while contador < 10:
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    numeros.append(numero)  # Agregar el número a la lista
    suma += numero  # Sumar el número al total
    contador += 1  # Incrementar el contador

# Calcular menor, mayor y promedio
menor = min(numeros)
mayor = max(numeros)
promedio = suma / len(numeros)

# Mostrar resultados
print(f"Menor: {menor}")
print(f"Mayor: {mayor}")
print(f"Promedio: {promedio:.2f}")  # Mostrar el promedio con 2 decimales