# Solicitar al usuario que ingrese un número
n = int(input("Ingrese un número para calcular su factorial: "))

# Verificar si el número es negativo
if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = 1  # Inicializa el resultado en 1
    contador = 1   # Inicializa el contador en 1

    while contador <= n:  # Mientras el contador sea menor o igual que n
        resultado *= contador  # Multiplica el resultado por el contador
        contador += 1  # Incrementa el contador

    print(f"El factorial de {n} es: {resultado}")  # Muestra el resultado final