import os 
os.system("cls")

productos = int(input("Cantidad de productos : "))

importe = productos * 20
descuento = 0
caramelos = 0

if productos > 700 :
    descuento = 0.16 * importe
elif productos >= 501 and productos <= 700 :
    descuento = 0.14 * importe
elif productos <= 500 :
    descuento = 0.12 * importe

total = importe - descuento

if productos >= 1 and productos <= 50:
    caramelos = 5
elif productos >= 51 and productos <= 100 :
    caramelos = 10
elif productos > 100 :
    caramelos = 15

print(f"El importe es : {importe:.2f}")
print(f"Descuento : {descuento:.2f}")
print(f"A pagar : {total:.2f}")
print(f"Caramelos adquiridos : {caramelos:.2f}")
