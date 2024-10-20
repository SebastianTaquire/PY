import os
os.system("cls")

def es_capicua(numero): 
    return str(numero) == str(numero)[::-1]  

def contar_capicuas():
    contador = 0  
    numero = 100  

    while numero < 1000:  
        if es_capicua(numero):  
            contador += 1  
        numero += 1  

    print(f"Hay {contador} números capicúas de 3 cifras.")

if __name__ == "__main__":
    contar_capicuas()