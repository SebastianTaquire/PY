def es_capicua(numero):
    """Verifica si un número es capicúa."""
    return str(numero) == str(numero)[::-1]  # Compara el número con su reverso

def contar_capicuas():
    """Cuenta y muestra cuántos números capicúas hay de 3 cifras."""
    contador = 0  # Inicializa el contador en 0
    numero = 100  # Comienza desde el primer número de 3 cifras

    while numero < 1000:  # Mientras el número sea menor que 1000
        if es_capicua(numero):  # Si el número es capicúa
            contador += 1  # Incrementa el contador
        numero += 1  # Incrementa el número

    print(f"Hay {contador} números capicúas de 3 cifras.")

# Ejemplo de uso
if __name__ == "__main__":
    contar_capicuas()