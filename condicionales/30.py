import os
os.system("cls")

cuota = int(input("Ingrese el monto de la cuota mensual: "))
pago = int(input("Ingrese el día del pago (1 a 30): "))

descuento = 0
recargo = 0
pagar = cuota

if pago <= 10:
    descuento = max(5, cuota * 0.02)
    pagar -= descuento
    print(f"El cliente paga dentro de los primeros 10 días y recibe un descuento de: ${descuento:.2f}")
elif 11 <= pago <= 20:
    print("El cliente paga entre los días 11 y 20. No hay descuento ni recargo.")
else:
    recargo = max(10, cuota * 0.03)
    pagar += recargo
    print(f"El cliente paga después del día 20 y tiene un recargo de: ${recargo:.2f}")

print(f"El total a pagar es: ${pagar:.2f}")