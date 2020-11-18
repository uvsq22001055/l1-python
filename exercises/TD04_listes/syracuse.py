def syracuse(n):
    res = []
    while True:
        res.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return res


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max + 1):
        syracuse(i)
    return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range(1, n_max + 1)]


print(tempsVolListe(10))


liste_vol = tempsVolListe(10000)
vol_max = max(liste_vol)
print("temps de vol maximum", vol_max)
print("atteint par l'entier", liste_vol.index(vol_max) + 1)

print("Le temps de vol de", 3, "est", tempsVol(3))

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
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon"""
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
