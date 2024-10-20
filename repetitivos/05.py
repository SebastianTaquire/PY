# Solicitar al usuario que ingrese un número
n = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Inicializar el contador en 1
contador = 1

# Bucle while para generar la tabla de multiplicar
while contador <= 12:
    print(f"{n} x {contador} = {n * contador}")  # Mostrar el resultado
    contador += 1  # Incrementar el contador