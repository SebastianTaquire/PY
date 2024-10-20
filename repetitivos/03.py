import os
os.system("cls")

dividendo = int(input("Dividendo : "))
divisor = int(input("Divisor : "))

divisores = 1

while dividendo > divisor : 
    dividendo -= divisor
    divisores += 1

print(f"Divisores : {divisores}")