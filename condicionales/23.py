import os
os.system("cls")

matematica = int(input("Nota de matematica : "))
fisica = int(input("Ingrese nota de fisica : "))
print()

propina = 0
reloj = False

if matematica > 17:
    propina += 3
else:
    propina += 1

if fisica > 15:
    propina += 2
else:
    propina += 0.5

promedio = (matematica + fisica) / 2

if promedio > 16:
    reloj = True
    print("El promedio es mayor a 16")
    print("CONSEGUISTE EL RELOJ")

print()
print(f"La propina total es : {propina:.2f}")

