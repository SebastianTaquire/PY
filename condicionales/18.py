import os
os.system("cls")

donacion = int(input("Ingrese cantidad de donacion : $"))

salud = 0
niños = 0
bolsa = 0

if donacion >= 10000:
    salud = donacion * 0.30
    niños = donacion * 0.50
    bolsa= donacion - (salud + niños)
else :
    salud = donacion * 0.25
    niños = donacion * 0.60
    bolsa = donacion - (salud + niños)

print(f"Dinero para la salud : {salud:.2f}")
print(f"Dinero para los niños : {niños}")
print(f"Dinero para la bolsa : {bolsa:.2f}") 
