import os, math
os.system("cls")

cateto1 = int(input("Valor del primer cateto: "))
cateto2 = int(input("Valor del segundo cateto: "))

hipotenusa = int(math.sqrt(cateto1**2 + cateto2**2))

print("La hipotenusa del triángulo es :", hipotenusa)

#nota para recuerdo el "**" es para hacer elevaciones 