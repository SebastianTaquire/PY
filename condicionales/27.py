import os
os.system("cls")

ventas = int(input("Ingrese el monto total de ventas: S/. "))

basico = 600.0
comision = 0
bruto = 0
descuento = 0
neto = 0
obsequiados = 1

comision = ventas * 0.15

bruto = basico + comision

if bruto > 1800:
    descuento = bruto * 0.10  
else:
    descuento = bruto * 0.05  

neto = bruto - descuento

if ventas > 1000:
    obsequiados = 3  
else:
    obsequiados = 1  

print(f"Sueldo bruto:  {bruto:.2f}")
print(f"Descuento aplicado:  {descuento:.2f}")
print(f"Sueldo neto: {neto:.2f}")
print(f"Polos obsequiados: {obsequiados}")