import os
os.system("cls")

def suma_lista(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + suma_lista(lst[1:])

print(suma_lista([1, 2, 3, 4, 5])) 