def suma_cifras_pares_impares(numero):
    """Calcula la suma de cifras pares e impares de un número."""
    suma_pares = 0
    suma_impares = 0

    while numero > 0:
        cifra = numero % 10  # Obtiene la última cifra
        if cifra % 2 == 0:
            suma_pares += cifra  # Suma a cifras pares
        else:
            suma_impares += cifra  # Suma a cifras impares
        numero //= 10  # Elimina la última cifra

    return suma_pares, suma_impares

def encontrar_numeros():
    """Encuentra y muestra números de 4 cifras con la condición deseada."""
    numero = 1000  # Comienza desde el primer número de 4 cifras
    contador = 0  # Inicializa el contador

    while numero < 10000:  # Mientras el número sea menor que 10000
        suma_pares, suma_impares = suma_cifras_pares_impares(numero)  # Suma de cifras
        if suma_pares == suma_impares:  # Verifica la condición
            print(numero)  # Muestra el número encontrado
            contador += 1  # Incrementa el contador
        numero += 1  # Incrementa el número

    print(f"Total de números encontrados: {contador}")

# Ejemplo de uso
if __name__ == "__main__":
    encontrar_numeros()