def es_primo(numero):
    """Determina si un número es primo."""
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    divisor = 2  # Iniciar con el primer divisor
    while divisor * divisor <= numero:  # Solo verificar hasta la raíz cuadrada del número
        if numero % divisor == 0:  # Si el número es divisible por 'divisor'
            return False  # No es primo
        divisor += 1  # Incrementar el divisor

    return True  # Si no se encontró ningún divisor, es primo

# Ejemplo de uso
if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(num):
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")