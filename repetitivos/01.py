import os
os.system("cls")

dividendo = int(input("Dividendo : "))
divisor = int(input("Divisor : "))

cociente = 0
while dividendo >= divisor:
    cociente += 1
    dividendo -= divisor

print(f"El cociente es : {cociente}")
print(f"El residuo es : {dividendo}")