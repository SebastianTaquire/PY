import os
os.system("cls")


tramo1_km = float(input("Longitud del primer tramo en kilómetros: "))
tramo2_pies = float(input("Longitud del segundo tramo en pies: "))
tramo3_millas = float(input("Longitud del tercer tramo en millas: "))

tramo1_metros = tramo1_km * 1000 
tramo2_metros = tramo2_pies / 3.2808  
tramo3_metros = tramo3_millas * 1609  

total_metros = tramo1_metros + tramo2_metros + tramo3_metros

pies = total_metros * 3.2808
milla = total_metros / 1609

print(f"Total recorrido en metros: {total_metros:.2f} m")
print(f"Total recorrido en pies: {pies:.2f}")
print(f"Total recorrido en millas: {milla:.2f}")