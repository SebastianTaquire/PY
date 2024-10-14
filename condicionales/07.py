import os
os.system("cls")

a = int(input("Numero 1:"))
b = int(input("Numero 2:"))
c = int(input("Numero 3:"))

if a > b:
    if b > c:
        intermedio = b
    elif c > a:
        intermedio = a
    else:
        intermedio = c
else:
    if a > c:
        intermedio = c
    elif c > b :
        intermedio = b
    else:
        intermedio = a

print(f"El numero es : {intermedio}") 