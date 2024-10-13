import os
os.system("cls")

n1 = int(input("Numero 1 : "))
n2 = int(input("Numero 2 : "))
n3 = int(input("Numero 3 : "))
n4 = int(input("Numero 4 : "))
n5 = int(input("Numero 5 : "))

max1 = max(n1, n2, n3, n4, n5)
restantes = [n1, n2, n3, n4, n5]
restantes.remove(max1)
max2 = max(restantes)
restantes.remove(max2)
max3 = max(restantes)

promedio = (max1 + max2 + max3) / 3

print(f"Promedio es : {promedio:.2f}")

