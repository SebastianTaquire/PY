import os
os.system("cls")

compra = int(input("Ingrese el monto total de la compra: "))

prestamo = 0
interes = 0
empresa = 0

if compra > 5000:
    prestamo = compra * 0.30 
else:
    prestamo = compra * 0.20 

interes = prestamo * 0.10 

empresa = compra - prestamo

print(f"Préstamo solicitado: {prestamo:.2f}")
print(f"Interés del préstamo: {interes:.2f}")
print(f"Dinero que cubrirá la empresa: {empresa:.2f}")