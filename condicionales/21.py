import os
os.system("cls")

numero = int(input("Ingrese un numero de 4 cifras : "))

if numero >= 1000 and numero <=9999:
    estado = numero // 1000
    edad = (numero % 1000 ) // 10
    sexo = numero % 10

    if estado == 1:
        print("Soltero")
    if estado == 2:
        print("Casado")
    if estado == 3:
        print("Divorciado")
    if estado == 4:
        print("Viudo")

    
    if sexo == 1:
        print("Masculino")
    if sexo == 2:
        print("Femenino")


print(f"La edad es : {edad}")
