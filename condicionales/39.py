import os
os.system("cls")

def grado_eficiencia():
    ausencia = float(input("Ingrese horas de ausencia: "))
    defectuosos = int(input("Ingrese cantidad de tornillos defectuosos: "))
    no_defectuosos = int(input("Ingrese cantidad de tornillos no defectuosos: "))

    grado = 5  # Grado mínimo
    condiciones = 0

    if ausencia <= 1.5:
        condiciones += 1
    if defectuosos < 300:
        condiciones += 1
    if no_defectuosos > 10000:
        condiciones += 1

    if condiciones == 1:
        grado = 7
    elif condiciones == 2:
        grado = 8
    elif condiciones == 3:
        grado = 9
    elif condiciones == 1 and defectuosos < 300:
        grado = 12
    elif condiciones == 1 and no_defectuosos > 10000:
        grado = 13
    elif condiciones == 2 and no_defectuosos > 10000:
        grado = 15
    elif condiciones == 3:
        grado = 20

    print(f"Grado de Eficiencia: {grado}")

grado_eficiencia()