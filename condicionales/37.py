import os
os.system("cls")

def resultados_eleccion():
    votos_pamela = int(input("Ingrese los votos de Pamela: "))
    votos_carol = int(input("Ingrese los votos de Carol: "))
    votos_fanny = int(input("Ingrese los votos de Fanny: "))
    
    total_votos = votos_pamela + votos_carol + votos_fanny
    umbral = total_votos / 2 + 1

    if (votos_pamela == votos_carol == votos_fanny) or (votos_pamela == votos_carol and votos_carol == votos_fanny):
        print("Elección anulada")
    elif votos_pamela >= umbral:
        print("Pamela ganó")
    elif votos_carol >= umbral:
        print("Carol ganó")
    elif votos_fanny >= umbral:
        print("Fanny ganó")
    else:
        if votos_pamela > votos_carol and votos_pamela > votos_fanny:
            print("Pamela y Carol pasan a segunda vuelta")
        elif votos_carol > votos_pamela and votos_carol > votos_fanny:
            print("Carol y Fanny pasan a segunda vuelta")
        else:
            print("Fanny y Pamela pasan a segunda vuelta")

resultados_eleccion()