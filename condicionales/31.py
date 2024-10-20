import os
os.system("cls")

categoria = input("Ingrese la categoría del trabajador (A, B, C, D): ").upper()
trabajadas = int(input("Ingrese el número de horas trabajadas: "))

hora = 0

if categoria == 'A':
    hora = 21.00
elif categoria == 'B':
    hora = 19.50
elif categoria == 'C':
    hora = 17.00
elif categoria == 'D':
    hora = 15.50
else:
    print("Categoría inválida.")
    exit()

bruto = trabajadas * hora

if bruto > 2500:
    descuento = bruto * 0.20
else:
    descuento = bruto * 0.15

neto = bruto - descuento

print(f"Sueldo bruto: S/. {bruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {neto:.2f}")