import os
os.system("cls")

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))

if hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
    print("Error: La hora o los minutos ingresados son inválidos.")
else:
    if hora == 0:
        formato_12h = 12
        periodo = "AM"
    elif hora == 12:
        formato_12h = 12
        periodo = "PM"
    elif hora > 12:
        formato_12h = hora - 12
        periodo = "PM"
    else:
        formato_12h = hora
        periodo = "AM"

    print(f"La hora05 es: {formato_12h}:{minutos:02d} {periodo}")