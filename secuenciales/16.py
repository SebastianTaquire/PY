import os
os.system("cls")

horas = int(input("Horas trabajadas : "))
tarifa = int(input("Ingresa tarifa : "))

basico = horas * tarifa
bonificacion = basico * 0.20
bruto = basico + bonificacion
descuento = bruto * 0.10
neto = bruto - descuento

print(f"Sueldo basico : {basico:.2f}")
print(f"Sueldo bruto : {bruto:.2f}")
print(f"Sueldo neto : {neto:.2f}")