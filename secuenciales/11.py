import os
os.system("cls")

numero1 = int(input("Nunero 1: "))
numero2 = int(input("Numero 2: "))

cifra1 = numero1 // 100  
cifra2 = (numero1 % 100) // 10
cifra3 = numero1 % 10  

cifra4 = numero2 // 100  
cifra5 = (numero2 % 100) // 10
cifra6 = numero2 % 10  

numero1 = (cifra4 * 100) + (cifra2 * 10) + cifra6
numero2 = (cifra1 * 100) + (cifra5 * 10) + cifra3

print(f"Los números son: {numero1:.2f} y {numero2:.2f}")