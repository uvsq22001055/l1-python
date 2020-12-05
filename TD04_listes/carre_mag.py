carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(i)
    print('\n')


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si\
         toutes les lignes ont la même somme, et -1 sinon"""
    lenght = len(carre)
    list_somme = []
    for i in range(lenght):
        s = 0
        s += sum(carre[i])
        list_somme.append(s)
    if s * lenght != sum(list_somme):
        print("-1")
    else:
        print(s)


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si \
        toutes les colonnes ont la même somme, et -1 sinon """
    nb_colonne = len(carre)
    list_somme = []
    for i in range(len(carre)):
        s = 0
        for k in range(len(carre[i])):
            s += carre[k][i]
        list_somme.append(s)
    if s * nb_colonne != sum(list_somme):
        return -1
    else:
        return s


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les\
        2 diagonales ont la même somme, et -1 sinon """
    list_somme1 = []
    list_somme2 = []
    for i in range(len(carre)):
        s = 0
        s += carre[i][i]
        list_somme1.append(s)
    for i in range(len(carre)):
        s = 0
        s += carre[i][abs(i - (len(carre)) + 1)]
        list_somme2.append(s)

    if sum(list_somme2) != sum(list_somme1):
        return -1
    else:
        return sum(list_somme1)


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et \
        False sinon"""
    if testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre):
        return True
    else:
        return False


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de \
        1 à n^2 où n est la taille du carré, et False sinon """
    s = 0
    l_c = len(carre) ** 2
    for i in range(l_c):
        s += 1
    if s == l_c:
        return True
    else:
        return False


print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
