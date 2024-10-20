import os
os.system("cls")

bruto = int(input("Ingrese el sueldo bruto del empleado: S/. "))
hijos = int(input("Ingrese el número de hijos del empleado: "))

bonificacion = 0

if hijos > 0:
    bonificacion = (bruto * 0.125) + (hijos * 40) 
else:
    bonificacion = bruto * 0.10  

neto = bruto + bonificacion

print(f"Bonificación:  {bonificacion:.2f}")
print(f"Sueldo neto a pagar:  {neto:.2f}")