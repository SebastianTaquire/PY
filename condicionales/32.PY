import os
os.system("cls")

categoria = input("Ingrese la categoría del estudiante (A, B, C, D): ").upper()
promedio = int(input("Ingrese el promedio ponderado del ciclo anterior: "))

pension = 0
descuento = 0

if categoria == 'A':
    pension = 550
elif categoria == 'B':
    pension = 500
elif categoria == 'C':
    pension = 450
elif categoria == 'D':
    pension = 400
else:
    print("Categoría inválida.")
    exit()

if categoria == 'A':
    descuento = 0
elif categoria == 'B' and 14 <= promedio <= 15.99:
    descuento = pension * 0.10
elif categoria == 'C' and 16 <= promedio <= 17.99:
    descuento = pension * 0.12
elif categoria == 'D' and 18 <= promedio <= 20:
    descuento = pension * 0.15

nueva_pension = pension - descuento

print(f"Pensión actual: S/. {pension:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Nueva pensión: S/. {nueva_pension:.2f}")