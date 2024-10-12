import os
os.system("cls")

numero = int(input( "Numero :"))

if numero < 0:
    print("Negativo")
elif numero > 0:
    print("Positivo")
else:
    print("Cero")