import os
os.system("cls")

angulo = int(input("Grados del angulo : "))

if angulo == 0 :
    print("Angulo nulo")
elif angulo > 0 and angulo < 90:
    print("Angulo agudo")
elif angulo == 90:
    print("Angulo recto")
elif angulo > 90 and angulo < 180:
    print("Angulo obtuso")
elif angulo == 180 :
    print("Angulo llano")
elif angulo > 180 and angulo < 360 :
    print("Amgulo cóncavo")
elif angulo == 360:
    print("Angulo completo")
else:
    print("Angulo no valido")

print(f"El angulo es {angulo:.2f}°")