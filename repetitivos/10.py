import os
os.system("cls")
def suma_cifras_pares_impares(numero):
    suma_pares = 0
    suma_impares = 0

    while numero > 0:
        cifra = numero % 10 
        if cifra % 2 == 0:
            suma_pares += cifra  
        else:
            suma_impares += cifra  
        numero //= 10  

    return suma_pares, suma_impares

def encontrar_numeros():
    numero = 1000  
    contador = 0  
    while numero < 10000:  
        suma_pares, suma_impares = suma_cifras_pares_impares(numero)  
        if suma_pares == suma_impares:  
            print(numero)  
            contador += 1  
        numero += 1  

    print(f"Total de números encontrados: {contador}")

if __name__ == "__main__":
    encontrar_numeros()