import os
os.system("cls")

numeros = []
contador = 0
suma = 0

while contador < 10:
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    numeros.append(numero) 
    suma += numero  
    contador += 1 

menor = min(numeros)
mayor = max(numeros)
promedio = suma / len(numeros)

print(f"Menor: {menor}")
print(f"Mayor: {mayor}")
print(f"Promedio: {promedio:.2f}")  