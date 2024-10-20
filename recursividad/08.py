import os
os.system("cls")

def contar_digitos(n):
    if n == 0:
        return 0
    return 1 + contar_digitos(n // 10)

print(contar_digitos(12345))