def suma_multiplos_3_no_5(n):
    """Calcula la suma de múltiplos de 3 que no son múltiplos de 5, menores o iguales a n."""
    suma = 0  # Inicializa la suma en 0
    i = 1  # Comienza con el primer número entero

    while i <= n:  # Mientras i sea menor o igual a n
        if i % 3 == 0 and i % 5 != 0:  # Verifica si i es múltiplo de 3 y no de 5
            suma += i  # Suma i a la variable suma
        i += 1  # Incrementa i

    return suma  # Devuelve la suma final

# Ejemplo de uso
if __name__ == "__main__":
    try:
        n = int(input("Ingrese un número entero n: "))
        resultado = suma_multiplos_3_no_5(n)
        print(f"La suma de los múltiplos de 3 que no son múltiplos de 5, menores o iguales a {n}, es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")