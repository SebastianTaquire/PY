import os
os.system("cls")

def subconjuntos(lst):
    if len(lst) == 0:
        return [[]]
    menor_sub = subconjuntos(lst[1:])
    return menor_sub + [[lst[0]] + s for s in menor_sub]

print(subconjuntos([1, 2, 3])) 