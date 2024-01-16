# Algoritme 1: Høyeste tall i en liste

def høyeste(liste: list[int]):
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest

def n_høyeste(liste: list[int], n: int):
    høyeste_n = []
    for i in range(n):
         høyest = max(liste)
         liste.remove(høyest)
         høyeste_n.append(høyest)
    return høyeste_n

print(n_høyeste([1,2,3,-5,5,-4,3], 3))

def n_høyeste_alt(liste: list[int], n: int):
    sortert = sorted(liste, reverse=True)
        