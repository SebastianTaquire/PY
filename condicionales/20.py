import os
os.system("cls")

numero1 = int(input("Numero 1 : "))
numero2 = int(input("Numero 2 : "))
numero3 = int(input("Numero 3 : "))

if numero1 > numero2 and numero2 > numero3:
    print("Numero ingresados de forma descendente")
elif numero3 > numero2 and numero2 > numero1:
    print("Numero ingresado de manera ascendente")
else:
    print("Numero ingresados en desorden")