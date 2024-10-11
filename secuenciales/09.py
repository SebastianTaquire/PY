import os
os.system("cls")

numero = int( input("Numero: " ) )
c1 = numero // 1000
c2 = ( numero % 1000 ) // 100
c3 = ( (numero % 1000 ) % 100 ) // 10
c4 = numero % 10 

print(f"Suma = { (c1 + c2 + c3 + c4)}")