import os
os.system("cls")

vendido = int(input("Cantidad vendida : "))

sueldo1 = vendido * 0.10
bono = 0

if vendido > 5000:
    exceso = vendido - 5000
    bono = (exceso // 500) * 25

total = sueldo1 + bono

print(f"Sueldo base : {sueldo1:.2f}")
print(f"Bono : {bono:.2f}")
print(f"Sueldo total : {total:.2f}")