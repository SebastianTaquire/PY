import os
os.system("cls")
def mostrar_numeros():
    numero = 1  
    while numero <= 100:  
        for _ in range(10):
            if numero > 100:  
                break
            print(numero, end=' ')  
            numero += 1  
        print() 

if __name__ == "__main__":
    mostrar_numeros()   