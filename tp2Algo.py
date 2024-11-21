#question 1

def entasser(tas, n, i):
    while True:
        biggest = i  
        gauche = 2 * i + 1  
        droite = 2 * i + 2  
        if gauche < n and tas[gauche] > tas[biggest]:
            biggest = gauche
        if droite < n and tas[droite] > tas[biggest]:
            biggest = droite
        if biggest != i:
            tas[i], tas[biggest] = tas[biggest], tas[i]
        else:
            break

def construire_tas(tas):
    n = len(tas)
    for i in range(n // 2 - 1, -1, -1):
        entasser(tas, n, i)

#question 2

def tri_par_tas(tas):
    construire_tas(tas)
    n = len(tas)
    for i in range(n - 1, 0, -1):
        tas[0], tas[i] = tas[i], tas[0]
        temporary_tas = tas[:i]
        construire_tas(temporary_tas)    
        for j in range(i):
            tas[j] = temporary_tas[j]

#test 
tableau = [143, 222, 6, 74, 2, 8764, 33, 57, 35, 100]
    
construire_tas(tableau)
print("TASmax :", tableau)

tri_par_tas(tableau)
print("Tableau trié :", tableau)