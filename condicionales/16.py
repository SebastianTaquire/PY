import os
os.system("cls")

ingresoMensual = int( input("Ingreso mensual : "))
costoCasa = int( input( "Costo casa : " ) )

#Puede ser de este modo
if ingresoMensual < 1250 :
     cuotaInicial = 0.15 * costoCasa
     cuotaMensual = ( 0.85 * costoCasa ) / 120
else : 
     cuotaInicial = 0.30 * costoCasa
     cuotaMensual = ( 0.70 * costoCasa ) / 75

#O este modo
cuotaInicial = ( 0.15 if ingresoMensual < 1250 else 0.30 ) * costoCasa
cuotaMensual = ( 0.85 if ingresoMensual < 1250 else 0.70 ) * costoCasa / ( 120 if ingresoMensual < 1250 else 75 )

print(f"Cuota inicial = {cuotaInicial:.2f}")
print(f"Cuota mensual = {cuotaMensual:.2f}")