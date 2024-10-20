import os
os.system("cls")

def promedio_final():
    pc1 = int(input("Ingrese la nota de la práctica 1 de Matemática: ")) * 0.10
    pc2 = int(input("Ingrese la nota de la práctica 2 de Matemática: ")) * 0.20
    pc3 = int(input("Ingrese la nota de la práctica 3 de Matemática: ")) * 0.10
    ep = int(input("Ingrese la nota del examen parcial de Matemática: ")) * 0.30
    ef = int(input("Ingrese la nota del examen final de Matemática: ")) * 0.30

    matematica = pc1 + pc2 + pc3 + ep + ef

    if matematica >= 13:
        estado = "Aprobado"
    else:
        estado = "Desaprobado"

    print(f"Promedio Final de Matemática: {matematica:.2f} - Estado: {estado}")

promedio_final()