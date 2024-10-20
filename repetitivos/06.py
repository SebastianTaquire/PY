n = int(input("Ingrese un número para generar su tabla de multiplicar: "))
x = int(input("Ingrese el inicio del rango (x): "))
y = int(input("Ingrese el fin del rango (y): "))

# Verificar si el rango es válido
if x > y:
    print("El inicio del rango debe ser menor o igual que el fin del rango.")
else:
    print(f"Tabla de multiplicar del {n} del {x} al {y}:")
    
    # Inicializar el contador en x
    contador = x

    while contador <= y:  # Mientras el contador sea menor o igual a y
        resultado = n * contador  # Calcular el resultado de la multiplicación
        print(f"{n} x {contador} = {resultado}")  # Mostrar el resultado
        contador += 1  # Incrementar el contador