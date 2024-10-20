import os
os.system("cls")

def longitud_lista(lst):
    if lst == []:
        return 0
    return 1 + longitud_lista(lst[1:])

print(longitud_lista([1, 2, 3, 4])) 