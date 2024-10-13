import os
os.system("cls")

basico = 500
comision = 0.09
descuento = 0.11

vendido = int(input("Ingrese cantidad vendida : "))

comisionM = vendido * comision

bruto = basico + comisionM

descuento = bruto * descuento

neto = bruto - descuento

print(f"Comision : {comisionM:.2f}")
print(f"Sueldo bruto : {bruto:.2f}")
print(f"Descuento : {descuento:.2f}")
print(f"Sueldo neto : {neto:.2f}")