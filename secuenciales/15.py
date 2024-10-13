import os
os.system("cls")

juan = int(input("Cantidad de juan : "))
rosa = int(input("Cantidad de rosa : "))
daniel = int(input("Cantidad de daniel soles : "))

daniel_dolares = daniel / 3 
capital = juan + rosa + daniel_dolares

p_juan = (juan / capital) * 100
p_rosa = (rosa / capital) * 100
p_daniel = (daniel_dolares / capital) * 100

print(f"Dolar Daniel : {daniel_dolares:.2f}")

print(f"La capital es : ${capital:.2f}")
print(f"Porcentaje de juan : {p_juan:.2f}")
print(f"Porcentaje de rosa : {p_rosa:.2f}")
print(f"Porcentaje de daniel : {p_daniel:.2f}")