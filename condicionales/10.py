import os
os.system("cls")

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
nota4 = int(input("Nota 4: "))
nota5 = int(input("Nota 5: "))

mayor = nota1
menor = nota1

if nota2 > mayor:
    mayor = nota2
if nota3 > mayor:
    mayor = nota3
if nota4 > mayor:
    mayor = nota4
if nota5 > mayor:
    mayor = nota5

if nota2 < menor:
    menor = nota2
if nota3 < menor:
    menor = nota3
if nota4 < menor:
    menor = nota4
if nota5 < menor:
    menor = nota5

total = 0
contador = 0

if nota1 == mayor:
    pass
elif nota1 == menor:
    pass
else:
    total += nota1
    contador += 1

if nota2 == mayor:
    pass
elif nota2 == menor:
    pass
else:
    total += nota2
    contador += 1

if nota3 == mayor:
    pass
elif nota3 == menor:
    pass
else:
    total += nota3
    contador += 1    

if nota4 == mayor:
    pass
elif nota4 == menor:
    pass
else:
    total += nota4
    contador += 1

if nota5 == mayor:
    pass
elif nota5 == menor:
    pass
else:
    total += nota5
    contador += 1

if contador > 0:
    promedio = total / contador

print(f"Nota mayor : {mayor}")
print(f"Nota menor : {menor}")
print(f"El promedio : {promedio:.2f}")