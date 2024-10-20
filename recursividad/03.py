import os
os.system("cls")

def maximo_lista(lst):
    if len(lst) == 1:
        return lst[0]
    max_rest = maximo_lista(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest

print(maximo_lista([3, 5, 1, 9, 2]))