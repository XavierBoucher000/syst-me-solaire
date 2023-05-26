import math



#système solaire


#on va devoir faire une boucle for pour calculer la position dans le temps






#On commence avec la position des planétes en conjoction avec le soleil.



# Constante gravitationnelle
G = 6.67430e-11  # m^3 kg^(-1) s^(-2)

# Masses des objets célestes en kilogrammes


#x[nom=0,masse=1,distance=2,vitesse=3]
x = [
    ('Soleil', 1.989e+30, [0, 0],  [0, 0]), 
    ('Mercure', 3.3011e+23, [57900000000.0, 0], [0, 47870.0]), 
    ('Venus', 4.8675e+24, [108200000000.0, 0 ], [0 ,35020.0]), 
    ('Terre', 5.97237e+24, [149600000000.0, 0 ], [0, 29780.0]), 
    ('Mars', 6.4171e+23, [227900000000.0 ,0], [0 ,24070.0]),
    ('Jupiter', 1.8982e+27, [778300000000.0,0,], [0 ,13070.0]), 
    ('Saturne', 5.6834e+26, [1427000000000.0, 0], [0 ,9690.0]), 
    ('Uranus', 8.681e+25, [2871000000000.0 ,0], [0 ,6810.0]), 
    ('Neptune', 1.02413e+26, [4498000000000.0,0], [0 ,5430.0])]
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
                    ao[l] += (x[i][1] * G) / ((x[i][2][l] - x[p][2][l]) ** 2)
        accelerations.append(ao)
    return accelerations



G = 6.67430e-11
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

liste_a = [
    [
        [2.8177416049460415e-07, 0], 
        [0.0395993661840819, 0], 
        [0.011339842539218936, 0], 
        [0.005932218682228908, 0], 
        [0.0025564813186421376, 0], 
        [0.00021924638299457728, 0], 
        [6.549677899909494e-05, 0], 
        [1.615530510702027e-05, 0], 
        [6.576885746337698e-06, 0]
    ]
]
liste_p = [[[0, 0], [57900000000.0, 0], [108200000000.0, 0], [149600000000.0, 0], 
            [227900000000.0, 0], [778300000000.0, 0], [1427000000000.0, 0], 
            [2871000000000.0, 0], [4498000000000.0, 0]]]
liste_v = [
    [[0, 0], [0, 0.5541203703703704], [0, 0.40564814814814813], [0, 0.3448148148148148],
    [0, 0.2799537037037037], [0, 0.15106481481481482], [0, 0.11215277777777777],
    [0, 0.07847222222222222], [0, 0.0625]]
]



def pop(temps):
    liste_vit_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    liste_pos_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    liste_acc_vide = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
    
    for t in range(1, temps+1):
        
        for planet in range(9):
            for coordonné in range(2):
                liste_pos_vide[planet][coordonné] = liste_p[t-1][planet][coordonné] + \
                                           liste_v[t-1][planet][coordonné] * 1 - \
                                           ((1**2 / 2) * liste_a[t-1][planet][coordonné])
        liste_p.append(liste_pos_vide)
        
        for planet in range(9):
            for coordonné in range(2):
                liste_vit_vide[planet][coordonné] = liste_v[t-1][planet][coordonné] + \
                                                    ((1) * liste_a[t-1][planet][coordonné])
        liste_v.append(liste_vit_vide)
        
        for pla_autre in range(9):
            for planete_propre in range(9):
                if x[pla_autre][1] != x[planete_propre][1]:

                    dx = liste_p[t][pla_autre][0] - liste_p[t][planete_propre][0]
                    dy = liste_p[t][pla_autre][1] - liste_p[t][planete_propre][1]
                    distance_squared = dx**2 + dy**2
                    angle = math.atan2(dy, dx)
                    liste_acc_vide[planete_propre][0] += (x[pla_autre][1] * G) / distance_squared
                    lol = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                    for i in range(len(liste_acc_vide)):
                        lol[i][0] = math.sin(angle)*liste_acc_vide[i][0]
                        lol[i][1] = math.cos(angle)*liste_acc_vide[i][0]
        liste_a.append(lol)
    return liste_p[365]

print(pop(365))