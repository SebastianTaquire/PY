import os
os.system("cls")

trabajadas = int(input("Ingrese el número de horas trabajadas: "))
hora = int(input("Ingrese el pago por hora: "))

normales = 0
extras = 0
extras = 1.20 

if trabajadas > 48:
    normales = 48
    extras = trabajadas - 48
else:
    normales = trabajadas
    horas_extras = 0

bruto = (normales * hora) + (extras * hora * extras)

descuento = 0
if bruto > 1500:
    descuento = bruto * 0.11 

neto = bruto - descuento

# Resultados
print(f"Horas trabajadas: {trabajadas}")
print(f"Pago por hora: S/. {hora:.2f}")
print(f"Sueldo bruto: S/. {bruto:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Sueldo neto a pagar: S/. {neto:.2f}")