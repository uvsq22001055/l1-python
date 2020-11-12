def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    print(n)
    while n != 1:

        if n % 2 == 0:
            n /= 2
            print(n)
        else:
            n = (n * 3) + 1
            print(n)
    print("\n")


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(1, n_max):
        syracuse(i)
    print("TRUE")


print(testeConjecture(10))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    pass


print("Le temps de vol de", 3, "est", tempsVol(3))
# Carré Magique
# 34
