import os
os.system("cls")

def obsequio_lapiceros():
    cuadernos = int(input("Ingrese el número de cuadernos adquiridos: "))

    if cuadernos < 12:
        lapiceros = 0
    elif 12 <= cuadernos < 24:
        lapiceros = cuadernos // 4
    elif 24 <= cuadernos < 36:
        lapiceros = 2 * (cuadernos // 4)
    else:
        lapiceros = 2 * (cuadernos // 4) + (cuadernos // 6) + (cuadernos // 12)

    print(f"Número de lapiceros obsequiados: {lapiceros}")

obsequio_lapiceros()