import os
os.system("cls")

def potencia(n, m):
    resultado = 1  
    contador = 0   

    while contador < m: 
        resultado *= n  
        contador += 1   
    return resultado  

if __name__ == "__main__":
    n = int(input("Ingrese el número base (n): "))
    m = int(input("Ingrese el exponente (m): "))
    resultado = potencia(n, m)
    print(f"{n} elevado a {m} es: {resultado}")