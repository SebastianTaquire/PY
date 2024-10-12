import os
os.system("cls")

gb = int(input("Gb :") )

mb = gb * 1024
kb = mb * 1024
bytes = kb * 1024

print(f"Mb : {mb:.2f}")
print(f"Kb : {kb:.2f}")
print(f"Bytes : {bytes:.2f}")