import os
os.system("cls")

def clasificar_empleado():
    codigo = int(input("Ingrese el código del empleado (3 cifras): "))

    if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0:
        tipo = "Administrativo"
    elif codigo % 3 == 0 and codigo % 5 == 0:
        tipo = "Directivo"
    elif codigo % 2 == 0:
        tipo = "Vendedor"
    else:
        tipo = "Seguridad"

    print(f"Tipo de Empleado: {tipo}")

clasificar_empleado()