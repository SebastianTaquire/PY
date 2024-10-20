import os
os.system("cls")

def contar_ocurrencias(lst, elem):
    if len(lst) == 0:
        return 0
    return (1 if lst[0] == elem else 0) + contar_ocurrencias(lst[1:], elem)

print(contar_ocurrencias([1, 2, 3, 1, 4, 1], 1)) 