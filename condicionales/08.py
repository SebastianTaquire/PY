import os
os.system("cls")

examen1 = int(input("Nota 1 : "))
examen2 = int(input("Nota 2 : "))
examen3 = int(input("Nota 3 : "))

propina = 20
aumento = 0
if examen1 >= 11:
    aumento += 5
if examen2 >= 11:
    aumento += 5
if examen3 >= 11:
    aumento += 5

total = propina + aumento

print(f"La propina total es : {total}")
