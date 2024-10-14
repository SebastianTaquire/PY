import os
os.system("cls")

unidades = int(input("Cantidad de unidades : "))

precio = 0
descuento = 0

if unidades >= 1 and unidades <= 25 :
    precio = 27
elif unidades >= 26 and unidades <= 50 :
    precio = 25
elif unidades >= 51:
    precio = 23

importe = unidades * precio

if unidades >= 50 :
    descuento = 0.15 * importe
elif unidades <= 49 :
    descuento = 0.09 * importe

total = importe - descuento

print(f"Importe : {importe:.2f}")
print(f"El descuento es : {descuento:.2f}")
print(f"Por pagar : {total:.2f}")