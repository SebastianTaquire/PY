import os
os.system("cls")

horas = int(input("Horas trabajadas : "))
tarifa = int(input("Ingresa tarifa : "))

basico = horas * tarifa

bruto = basico * 0.20
neto = bruto * 0.10

print(f"Sueldo basico : {basico:.2f}")
print(f"Sueldo bruto : {bruto:.2f}")
print(f"Sueldo neto : {neto:.2f}")