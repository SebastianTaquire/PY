import os
os.system("cls")

def multiplica(n1, n2):
    if n2 == 1: return n1
    return n1 + multiplica(n1, n2-1)

multiplicando= int(input("Ingrese numero 1 : "))
multiplicador = int(input("Ingrese numero 2 : "))

print(f"Producto : {multiplica(multiplicando, multiplicador)}")

def multiplica(n1,n2):
    producto = 0
    while n2>0:
        n2 -= 1
        producto += n1
    return producto

producto = 0
while multiplicador > 0:
    multiplicador -= 1
    producto += multiplicando

print(f"Producto es : {producto}")
