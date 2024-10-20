import os
os.system("cls")

def suma_multiplos_3_no_5(n):
    suma = 0 
    i = 1  

    while i <= n: 
        if i % 3 == 0 and i % 5 != 0:  
            suma += i  
        i += 1  

    return suma  

if __name__ == "__main__":
    try:
        n = int(input("Ingrese un número entero n: "))
        resultado = suma_multiplos_3_no_5(n)
        print(f"La suma de los múltiplos de 3 que no son múltiplos de 5, menores o iguales a {n}, es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")