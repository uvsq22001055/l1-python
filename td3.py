#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    temps = temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]
    return temps


temps = (3,23,1,34)
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


def demandeTemps():
    pass


def sommeTemps(temps1,temps2):
    s1 = tempsEnSeconde(temps1)
    s2 = tempsEnSeconde(temps2)
    st  = s1 + s2
    print(secondeEnTemps(st))
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
    s = (((s % 31536000) % 86400) % 3600) % 60
    temps =  (a, j, h, mn, s)
    return temps


def afficheDate(temps):
    

    if temps [1] == 1:
            print (temps[1], "jour ", end="")
    elif temps [1] == 0:
            print(end="")
    else:
            print (temps[1], "jours ", end="")

    print(temps[0]," à ")

    if temps [2] == 1:
            print (temps[2], "heure ", end="")
    elif temps [2] == 0:
            print(end="")
    else: 
            print (temps[2], "heures ", end="")

    if temps [3] == 1:
            print (temps[3], "minute ", end="")
    elif temps [3] == 0:
            print(end="")
    else:
            print (temps[3], "minutes ", end="")

    if temps [4] == 1:
            print (temps[4], "seconde ", end="")
    elif temps [4] == 0:
            print(end="")
    else:
            print (temps[4], "secondes ", end="")
    return afficheDate

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()