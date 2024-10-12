import os
os.system("cls")

pies = int(input("Pies: "))
pulgadas = int(input("Pulgadas: "))

metros_pies = pies * 0.3048
metros_pulgadas = pulgadas * 0.0254
estatura = metros_pies + metros_pulgadas 

print(f"Estatura : {estatura:.2f}")