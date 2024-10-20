import os
os.system("cls")

def mostrar_rectangulo(n):
    if n < 4:
        print("El valor de n debe ser mayor o igual a 4.")
        return

    altura = 0 

    while altura < n:  
        ancho = 0  
        while ancho < 2 * n:  
            print("*", end="")  
            ancho += 1  
        print()  
        altura += 1  

if __name__ == "__main__":
    n = int(input("Ingrese el valor de n (n >= 4): "))
    mostrar_rectangulo(n)