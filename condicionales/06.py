import os
os.system("cls")

numero = int(input("Ingresa numero : "))

if numero >= 1000 and numero <= 9999 :
    digito1 = numero // 1000
    digito2 = (numero % 1000) // 100
    digito3 = ((numero % 1000) % 100) // 10
    digito4 = numero % 10
    
    mayor = digito1
    minimo = digito1

    if digito2 > mayor:
        mayor = digito2
    elif digito3 > mayor:
        mayor = digito3
    elif digito4 > mayor:
        mayor = digito4
    
    if digito2 < minimo:
        minimo = digito2
    elif digito3 < minimo:
        minimo = digito3
    elif digito4<minimo:
        minimo = digito4


    print(f"El mayor numero es: {mayor}{minimo}")

else:
    print("No es numero de 4 cifras")  