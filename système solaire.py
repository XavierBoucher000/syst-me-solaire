import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pickle

#système solaire

#on va devoir faire une boucle for pour calculer la position dans le temps






#On commence avec la position des planétes en conjoction avec le soleil.



# Constante gravitationnelle
G = 6.67430e-11  # m^3 kg^(-1) s^(-2)

    # Masses des objets célestes en kilogrammes


    #x[nom=0,masse=1,distance=2,vitesse=3]
x = [
        ('Soleil', 1.989e+30, [0, 0], [0, 0]), 
        ('Mercure', 3.3011e+23, [-69816900000.0, 0], [0, 38860.0]), 
        ('Venus', 4.8675e+24, [-108942109000.0, 0], [0, 34790.0]), 
        ('Terre', 5.97237e+24, [-152097701000.0, 0], [0, 29290.0]), 
        ('Mars', 6.4171e+23, [-249232432000.0, 0], [0, 24130.0]),
        ('Jupiter', 1.8982e+27, [-816520800000.0, 0], [0, 13070.0]), 
        ('Saturne', 5.6834e+26, [-1513325783000.0, 0], [0, 9690.0]), 
        ('Uranus', 8.681e+25, [-3002962242000.0, 0], [0, 6810.0]), 
        ('Neptune', 1.02413e+26, [-4546599342000.0, 0], [0, 5430.0])
    ]

    # le module de distance entre les astres est:


def acc():
        accelerations = []
        for p in range(len(x)):
            ao = [0, 0]
            for l in range(2):
                for i in range(len(x)):
                    if x[p][1] == x[i][1]:
                        continue
                    elif x[i][2][l] == 0 and x[p][2][l] == 0:
                        continue
                    else:
                        ao[l] += (-x[i][1] * G) / ((x[i][2][l] - x[p][2][l]) ** 2)
            accelerations.append(ao)
        return accelerations





G = 6.67430e-11 * 3600  # Convert G to m^3/(kg min^2)

x = [
    ('Soleil', 1.989e+30),
    ('Mercure', 3.3011e+23),
    ('Venus', 4.8675e+24),
    ('Terre', 5.97237e+24),
    ('Mars', 6.4171e+23),
    ('Jupiter', 1.8982e+27),
    ('Saturne', 5.6834e+26),
    ('Uranus', 8.681e+25),
    ('Neptune', 1.02413e+26)
]

def pop(temps):
    liste_p = [[[0, 0],[-69788000000, 0], [-108942109000.0, 0], [-152097701000.0, 0], [-249232432000.0, 0], [-816520800000.0, 0], [-1513325783000.0, 0], [-3002962242000.0, 0], [-4546599342000.0, 0]]]
    liste_v = [[[0, 0], [0, 38860.0 * 60], [0, 34790.0 * 60], [0, 29290.0 * 60], [0, 24130.0 * 60], [0, 13070.0 * 60], [0, 9690.0 * 60], [0, 6810.0 * 60], [0, 5430.0 * 60]]]
    liste_a =[[[2.573758994586464e-07 * 60**2, 0], [0.0272350174643321 * 60**2, 0], [0.011185837735617765 * 60**2, 0], [0.005738948755460302 * 60**2, 0], [0.0021376102291935056 * 60**2, 0], [0.00019919748084896058 * 60**2, 0], [5.823101042404175e-05 * 60**2, 0], [1.4767677593284985e-05 * 60**2, 0], [6.437653783803956e-06 * 60**2, 0]]]
    
    for t in range(1, temps + 1):
        liste_pos_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[0, 0]]
        liste_vit_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[0, 0]]
        liste_acc_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[0, 0]]
        for planet in range(9):
            for coordonné in range(2):
                liste_pos_vide[planet][coordonné] = liste_p[t-1][planet][coordonné] + liste_v[t-1][planet][coordonné]+(0.5* liste_a[t-1][planet][coordonné])
                liste_vit_vide[planet][coordonné] = liste_v[t-1][planet][coordonné] + liste_a[t-1][planet][coordonné]
        liste_p.append(liste_pos_vide)
        liste_v.append(liste_vit_vide)
        for pla_autre in range(9):
            for planete_propre in range(9):
                if x[pla_autre][1] == x[planete_propre][1]:
                    continue
                else:
                    distx = (liste_p[t][pla_autre][0] - liste_p[t][planete_propre][0])
                    disty = (liste_p[t][pla_autre][1] - liste_p[t][planete_propre][1])
                    angle = math.atan2(disty,distx)
                    DIST = ((distx ** 2) + (disty) ** 2)
                    liste_acc_vide[planete_propre][0] += (math.cos(angle)*(x[pla_autre][1] * G) / DIST)
                    liste_acc_vide[planete_propre][1] += (math.sin(angle)*(x[pla_autre][1] * G) / DIST)
        liste_a.append(liste_acc_vide)
        print(temps-t)
        
    return liste_p
result = (pop(60*24*90))


# Save the result to a file using NumPy save()

np.save('result.npy', result)
print('Hello mother')