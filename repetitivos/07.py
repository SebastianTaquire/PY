import os
os.system("cls")

def factorial( n ):
    factorial = 1
    while n>1:
        rpta *= n
        n -=1
    return rpta

numero = int(input("Numero : "))

factorial = 1

while numero > 0:
    factorial *= numero
    numero -= 1

print(f"Factorial : {factorial}")