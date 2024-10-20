def mostrar_numeros():
    """Muestra los números del 1 al 100, 10 por fila."""
    numero = 1  # Inicializa el contador en 1
    while numero <= 100:  # Mientras el número sea menor o igual a 100
        # Imprime los próximos 10 números
        for _ in range(10):
            if numero > 100:  # Si el número supera 100, salimos del bucle
                break
            print(numero, end=' ')  # Imprime el número en la misma línea
            numero += 1  # Incrementa el número
        print()  # Salto de línea después de cada fila

# Ejemplo de uso
if __name__ == "__main__":
    mostrar_numeros()   