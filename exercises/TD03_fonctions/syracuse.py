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


print(syracuse(3))
