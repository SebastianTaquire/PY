import os
os.system("cls")

edad1 = int(input("Ingrese edad 1 : "))
edad2 = int(input("Ingrese edad 2 : "))
edad3 = int(input("Ingrese edad 3 : "))

menor = edad1
mayor = edad1

if edad2 > mayor:
    mayor = edad2
if edad3 > mayor:
    mayor = edad3

if edad2 < menor:
    menor = edad2
if edad3 < menor:
    menor = edad3

print()
print(f"La edad mayor es : {mayor}")
print(f"La edad menor es : {menor}")