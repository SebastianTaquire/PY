def potencia(n, m):
    """Calcula n elevado a m utilizando un bucle while."""
    resultado = 1  # Inicializa el resultado en 1
    contador = 0   # Inicializa el contador

    while contador < m:  # Mientras el contador sea menor que m
        resultado *= n  # Multiplica el resultado por n
        contador += 1   # Incrementa el contador

    return resultado  # Devuelve el resultado final

# Ejemplo de uso
if __name__ == "__main__":
    n = int(input("Ingrese el número base (n): "))
    m = int(input("Ingrese el exponente (m): "))
    resultado = potencia(n, m)
    print(f"{n} elevado a {m} es: {resultado}")