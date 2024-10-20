import os
os.system("cls")

def es_primo(numero):
    if numero <= 1:
        return False  

    divisor = 2 
    while divisor * divisor <= numero: 
        if numero % divisor == 0: 
            return False  
        divisor += 1  

    return True  

if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(num):
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")