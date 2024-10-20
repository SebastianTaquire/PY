import os
os.system("cls")
n = int(input("Ingrese un número para generar su tabla de multiplicar: "))
x = int(input("Ingrese el inicio del rango (x): "))
y = int(input("Ingrese el fin del rango (y): "))

if x > y:
    print("El inicio del rango debe ser menor o igual que el fin del rango.")
else:
    print(f"Tabla de multiplicar del {n} del {x} al {y}:")
    
    contador = x

    while contador <= y: 
        resultado = n * contador 
        print(f"{n} x {contador} = {resultado}")  
        contador += 1  