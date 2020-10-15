#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    return temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
   return temps
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici


def afficheTemps (temps):


    if temps [0] == 1:
            print (temps[0], "jour ", end="")
    elif temps [0] == 0:
            print(end="")
    else:
            print (temps[0], "jours ", end="")

    if temps [1] == 1:
            print (temps[1], "heure ", end="")
    elif temps [1] == 0:
            print(end="")
    else:
            print (temps[1], "heures ", end="")

    if temps [2] == 1:
            print (temps[2], "minute ", end="")
    elif temps [2] == 0:
            print(end="")
    else:
            print (temps[2], "minutes ", end="")

    if temps [3] == 1:
            print (temps[3], "seconde ", end="")
    elif temps [3] == 0:
            print(end="")
    else:
            print (temps[3], "secondes ", end="")
    return afficheTemps

afficheTemps((1,0,14,23))  