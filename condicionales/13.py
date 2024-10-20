import os
os.system("cls")

numero = int(input("Ingrese numero de 3 cifras : "))

if numero < 1000 and numero > 99:
    digito1 = numero // 100
    digito2 = (numero % 100) // 10
    digito3 = numero % 10

    if digito1 > digito2 and digito2 > digito3: 
        print("Esta de modo descendente")
    
    elif digito1 < digito2 and digito2 < digito3:
        print("Esta de modo ascendente")
    
    else:
        print("Esta desordenado")

else:
    print()
    print("Por favor ingresa un numero de 3 cifras positivos")