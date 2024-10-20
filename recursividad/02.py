import os
os.system("cls")

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    return invertir_cadena(cadena[1:]) + cadena[0]

print(invertir_cadena("python")) 