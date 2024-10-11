import os
os.system("cls")

cantidad = int(input("Ingrese la cantidad de dinero : ") )

billetes_200 = cantidad // 200
cantidad %= 200
billetes_100 = cantidad // 100
cantidad %= 100
billetes_50 = cantidad // 50
cantidad %= 50
billetes_20 = cantidad // 20
cantidad %= 20
billetes_10 = cantidad // 10
cantidad %= 10
monedas_5 = cantidad // 5
cantidad %= 5
monedas_2 = cantidad // 2
cantidad %= 2
monedas_1 = cantidad // 1

print(f"Billetes de 200: {billetes_200:.2f}")
print(f"Billetes de 100: {billetes_100:.2f}")
print(f"Billetes de 50: {billetes_50:.2f}")
print(f"Billetes de 20: {billetes_20:.2f}")
print(f"Billetes de 10: {billetes_10:.2f}")
print(f"Monedas de 5: {monedas_5:.2f}")
print(f"Monedas de 2: {monedas_2:2f}")
print(f"Monedas de 1: {monedas_1:.2f}")