import os
os.system("cls")

A = 25
B = 30 

productosA = int(input("Ingrese cantidad de productos A : "))
print()
productosB = int(input("Ingrese cantidad de productos B : "))

brutoA = productosA * A
brutoB = productosB * B

descuentoA = 0
descuentoB = 0

if  productosA > 50:
    descuentoA = brutoA * 0.15
if productosB > 60:
    descuentoB = brutoB * 0.10 

totalA = brutoA - descuentoA
totalB = brutoB - descuentoB

total = totalA + totalB

print(f"Importe bruto A : {brutoA}")
print(f"Importe bruto B : {brutoB}")
print()
print(f"Descuento de A es : {descuentoA:.2f}")
print(f"Descuento de B es : {descuentoB:.2f}")
print()
print(f"Total a pagar : {total:.2f}")