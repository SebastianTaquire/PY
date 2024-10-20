import os
os.system("cls")

def dias_y_mes():
    mes = int(input("Ingrese el mes (1-12): "))
    anio = int(input("Ingrese el año: "))
    dias = 0
    nombre_mes = ""

    if mes == 1:
        nombre_mes = "Enero"
        dias = 31
    elif mes == 2:
        nombre_mes = "Febrero"
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias = 29
        else:
            dias = 28
    elif mes == 3:
        nombre_mes = "Marzo"
        dias = 31
    elif mes == 4:
        nombre_mes = "Abril"
        dias = 30
    elif mes == 5:
        nombre_mes = "Mayo"
        dias = 31
    elif mes == 6:
        nombre_mes = "Junio"
        dias = 30
    elif mes == 7:
        nombre_mes = "Julio"
        dias = 31
    elif mes == 8:
        nombre_mes = "Agosto"
        dias = 31
    elif mes == 9:
        nombre_mes = "Septiembre"
        dias = 30
    elif mes == 10:
        nombre_mes = "Octubre"
        dias = 31
    elif mes == 11:
        nombre_mes = "Noviembre"
        dias = 30
    elif mes == 12:
        nombre_mes = "Diciembre"
        dias = 31
    else:
        print("Mes inválido.")
        return

    print(f"Mes: {nombre_mes}, Días: {dias}")

dias_y_mes()