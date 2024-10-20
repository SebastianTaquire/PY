def mostrar_rectangulo(n):
    """Muestra un rectángulo de asteriscos de altura n y ancho 2n."""
    if n < 4:
        print("El valor de n debe ser mayor o igual a 4.")
        return

    altura = 0  # Inicializa la altura del rectángulo

    while altura < n:  # Mientras la altura sea menor que n
        ancho = 0  # Inicializa el ancho en cada nueva fila
        while ancho < 2 * n:  # Mientras el ancho sea menor que 2n
            print("*", end="")  # Imprime un asterisco sin salto de línea
            ancho += 1  # Incrementa el ancho
        print()  # Salto de línea al finalizar una fila
        altura += 1  # Incrementa la altura

# Ejemplo de uso
if __name__ == "__main__":
    n = int(input("Ingrese el valor de n (n >= 4): "))
    mostrar_rectangulo(n)