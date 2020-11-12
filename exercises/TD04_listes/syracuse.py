def syracuse(n):
    res = []
    while True :
        res.append(n)
        if n == 1:
             break
        if n % 2 == 0:
            n = n //2
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


print("Le temps de vol de", 3, "est", tempsVol(3))
# Carré Magique
# 34
