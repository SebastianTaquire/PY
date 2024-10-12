import os, math
os.system("cls")

radio = int(input("Radio : "))
altura = int(input("Altura : "))

areabase = math.pi * radio**2
arealateral = 2 * math.pi * radio * altura
areatotal = 2 * areabase + arealateral

print(f"AreaBase : {areabase:.2f}")
print(f"AreaLateral : {arealateral:.2f}")
print(f"AreaTotal : {areatotal:.2f}")