import os
os.system("cls")

basico = 250
vendido = int(input("Ingrese el monto vendido : "))
comision = 0

if vendido <= 5000:
    comision = vendido * 0.05
elif vendido > 5000 and vendido <=10000:
    comision = vendido * 0.08
elif vendido > 10000 and vendido <= 20000:
    comision = vendido * 0.10
elif vendido > 20000:
    comision = vendido * 0.15

bruto = basico + comision
descuento = 0

if bruto > 3500:
    descuento = bruto * 0.15
else:
    descuento = bruto * 0.08

neto = bruto - descuento

print()
print(f"Sueldo basico : {basico:.2f}")
print(f"Comision : {comision:.2f}")
print(f"Sueldo bruto : {bruto:.2f}")
print(f"Descuento : {descuento:.2f}")
print(f"Sueldo neto : {neto:.2f}")