import os
os.system("cls")
n = int(input("Ingrese un número para generar su tabla de multiplicar: "))

contador = 1

while contador <= 12:
    print(f"{n} x {contador} = {n * contador}")
    contador += 1