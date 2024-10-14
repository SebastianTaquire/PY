import os
os.system("cls")

codigo = int(input("Codigo de productos : "))
cantidad = int(input("Cantidad de productos : "))

precio = 0
descuento = 0

if codigo == 101:
    precio = 17
    if cantidad >=1 and cantidad <= 10:
        descuento = 0.05
    elif cantidad >=11 and cantidad <= 20:
        descuento = 0.08
    elif cantidad >= 21 and cantidad<=30:
        descuento =0.10
    elif cantidad >= 31:
        descuento = 0.13

elif codigo == 102:
    precio = 25
    if cantidad >=1 and cantidad <= 10:
        descuento = 0.05
    elif cantidad >=11 and cantidad <= 20:
        descuento = 0.08
    elif cantidad >= 21 and cantidad<=30:
        descuento =0.10
    elif cantidad >= 31:
        descuento = 0.13

elif codigo == 103:
    precio = 16
    if cantidad >=1 and cantidad <= 10:
        descuento = 0.05
    elif cantidad >=11 and cantidad <= 20:
        descuento = 0.08
    elif cantidad >= 21 and cantidad<=30:
        descuento =0.10
    elif cantidad >= 31:
        descuento = 0.13

elif codigo == 104:
    precio = 27
    if cantidad >=1 and cantidad <= 10:
        descuento = 0.05
    elif cantidad >=11 and cantidad <= 20:
        descuento = 0.08
    elif cantidad >= 21 and cantidad<=30:
        descuento =0.10
    elif cantidad >= 31:
        descuento = 0.13

importe = precio * cantidad
rebaja = descuento * importe
total = importe - rebaja

print(f"Importe : {importe}")
print(f"Descuento : {rebaja}")
print(f"Total a pagar : {total}")

