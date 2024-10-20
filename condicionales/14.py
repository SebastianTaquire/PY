import os
os.system("cls")

tarjeta = int(input("Ingrese numero de tarjeta : "))
compra = int(input("Monto de compra : "))

descuento = 0

if tarjeta % 2 == 0:
    if tarjeta >= 100:
        descuento = compra * 0.15
    else:
        descuento =  compra * 0.05
else:
    descuento =  compra * 0.05

pagar = compra - descuento

print()
print(f"Numero de la tarjeta : {tarjeta}")
print(f"Monto de la compra : {compra:.2f}")
print(f"Descuento : {descuento:.2f}")
print(f"A pagar : {pagar:.2f}")