def tempsEnSeconde(temps):
    temps = temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]
    return temps


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    j = seconde//86400
    h = (seconde % 86400) // 3600
    m = ((seconde % 86400) % 3600) // 60
    s = ((seconde % 86400) % 3600) % 60
    temps = (j, h, m, s)
    return temps


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes\n")

def afficheTemps (temps): 
    if temps[0] == 1:
        print(temps[0], "jour ", end="")
    elif temps[0] == 0:
        print(end="")
    else:
        print(temps[0], "jours ", end="")

    if temps[1] == 1:
        print(temps[1], "heure ", end="")
    elif temps[1] == 0:
        print(end="")
    else: 
        print(temps[1], "heures ", end="")

    if temps[2] == 1:
        print(temps[2], "minute ", end="")
    elif temps[2] == 0:
        print(end="")
    else:
        print(temps[2], "minutes ", end="")

    if temps[3] == 1:
        print (temps[3], "seconde ", end="")
    elif temps[3] == 0:
        print(end="")
    else:
        print(temps[3], "secondes\n ", end="")
    return afficheTemps

afficheTemps((1,0,14,23))


def demandeTemps():
    j = int(input("Nombre de jours"))
    while j < 0 :
        j = int(input("ERREUR choisir un nombre de jours POSITIF"))

    h = int(input("Nombre d'heures"))
    while h < 0 or h > 23 :
        h = int(input("ERREUR choisir un nombre d'heure compris entre 0 et 23"))

    m = int(input("Nombre de minutes"))
    while m < 0 or m > 59 :
        m = int(input("ERREUR choisir un nombre de minutes compris entre 0 et 59"))

    s = int(input("Choisir un nombre de seconde"))
    while s < 0 or s > 59 :
        s = int(input("ERREUR choisir un nombre de seconde compris entre 0 et 59"))

    temps = (j, h, m, s)
    return temps

demandeTemps()


def sommeTemps(temps1, temps2):
    s1 = tempsEnSeconde(temps1)
    s2 = tempsEnSeconde(temps2)
    s_t  = s1 + s2
    print(secondeEnTemps(s_t))
    return


sommeTemps((2,3,4,25),(5,22,57,1))


def proportionTemps(temps,proportion):
    temps_proportionne = int(tempsEnSeconde(temps) * proportion)
    temps = secondeEnTemps(temps_proportionne)
    return temps


afficheTemps(proportionTemps((2,0,36,0),0.2))


def tempsEnDate(temps):
    s = tempsEnSeconde(temps)
    a = s // 31536000
    j = (s % 31536000) // 86400
    h = ((s % 31536000) % 86400) // 3600
    mn = (((s % 31536000) % 86400) % 3600) // 60
    sec = (((s % 31536000) % 86400) % 3600) % 60
    temps = (a, j, h, mn, sec)
    return temps



def afficheDate(date = -1):
    temps_0 = (1970, 1, 00, 00, 00)
    if date == -1 :
        print("1 janvier 1970 à 00:00:00")
    else:
        if date [1] == 1:
            print (date[1] + 1,"ème jour de ", end="")
        elif date [1] == 0:
            print(end="")
        else:
            print (date[1] + 1,"ème jours de ", end="")

        print(date[0] + 1970,"à ", end="")

        if date [2] == 1:
            print (date[2], "heure ", end="")
        elif date [2] == 0:
            print(end="")
        else: 
            print (date[2], "heures ", end="")

        if date [3] == 1:
            print (date[3], "minute ", end="")
        elif date [3] == 0:
            print(end="")
        else:
            print (date[3], "minutes ", end="")

        if date [4] == 1:
            print (date[4], "seconde ", end="")
        elif date [4] == 0:
            print(end="")
        else:
            print (date[4], "secondes\n ")
    return afficheDate

    temps = secondeEnTemps(1000000000)

afficheDate()
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))



import time
import calendar
calendar.timegm(time.gmtime())

afficheDate(tempsEnDate(secondeEnTemps(calendar.timegm(time.gmtime()))))