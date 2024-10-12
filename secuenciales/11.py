import os
os.system("cls")

numero1 = int(input("Nunero 1: "))
numero2 = int(input("Numero 2: "))

# Descomponer el primer número en sus cifras
cifra1 = numero1 // 100  # Primera cifra
cifra2 = (numero1 // 10) % 10  # Segunda cifra
cifra3 = numero1 % 10  # Tercera cifra

# Descomponer el segundo número en sus cifras
cifra4 = numero2 // 100  # Primera cifra
cifra5 = (numero2 // 10) % 10  # Segunda cifra
cifra6 = numero2 % 10  # Tercera cifra

# Intercambiar la primera cifra del primer número con la tercera del segundo, y viceversa
numero1 = (cifra1 * 100) + (cifra2 * 10) + cifra3
numero2 = (cifra4 * 100) + (cifra5 * 10) + cifra6

# Imprimir los resultados
print(f"Los números son: {numero1:.2f} y {numero2:.2f}")