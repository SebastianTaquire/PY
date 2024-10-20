import os
os.system("cls")

compra = int(input("Cantidad de compra : "))
descuento = 0

if compra >= 6:
    descuento = compra * 0.15
else:
    descuento = compra * 0.10

pagar = compra - descuento

lapiceros = 0
if compra >= 30:
    lapiceros = (compra // 3) * 2

print(f"Monto de la compra : {compra:.2f}")
print(f"Descuento : {descuento:.2f}")
print(f"A pagar : {pagar:.2f}")
print(f"Cantidad de lapiceros : {lapiceros}")
