import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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







import math


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

def pop(temps):
    liste_p = [[[0, 0], [-57900000000.0, 0], [-108200000000.0, 0], [-149600000000.0, 0], 
            [-227900000000.0, 0], [-778300000000.0, 0], [-1427000000000.0, 0], 
            [-2871000000000.0, 0], [-4498000000000.0, 0]]]
    liste_v = [[[0, 0], [0, 47870.0], [0, 35020.0], [0, 29780.0], 
            [0, 24070.0], [0, 13070.0], [0, 9690.0], [0, 6810.0], [0, 5430.0]]]
    liste_a = [
        [
            [-2.8177416049460415e-07, 0], 
            [-0.0395993661840819, 0], 
            [-0.011339842539218936, 0], 
            [-0.005932218682228908, 0], 
            [-0.0025564813186421376, 0], 
            [-0.00021924638299457728, 0], 
            [-6.549677899909494e-05, 0], 
            [-1.615530510702027e-05, 0], 
            [-6.576885746337698e-06, 0]
        ]
    ]

    for t in range(1, temps + 1):
        liste_pos_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        liste_vit_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        liste_acc_vide = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        
        for planet in range(9):
            for coordonné in range(2):
                liste_pos_vide[planet][coordonné] = liste_p[t-1][planet][coordonné] + \
                                           liste_v[t-1][planet][coordonné] * 1 + \
                                           ((1**2 / 2) * liste_a[t-1][planet][coordonné])
                liste_vit_vide[planet][coordonné] = liste_v[t-1][planet][coordonné] + \
                                                    ((1) * liste_a[t-1][planet][coordonné])
        liste_p.append(liste_pos_vide)
        liste_v.append(liste_vit_vide)
        
        for pla_autre in range(9):
            for planete_propre in range(9):
                if x[pla_autre][1] == x[planete_propre][1]:
                    continue
                else:
                    angle = math.atan2((liste_p[t][pla_autre][0] - liste_p[t][planete_propre][0]), (liste_p[t][pla_autre][1] - liste_p[t][planete_propre][1]))
                    liste_acc_vide[planete_propre][0] += math.cos(angle)*(x[pla_autre][1] * -G) / (((liste_p[t][pla_autre][0] - liste_p[t][planete_propre][0]) ** 2) + ((liste_p[t][pla_autre][1] - liste_p[t][planete_propre][1]) ** 2))
                    liste_acc_vide[planete_propre][1] += math.sin(angle)*(x[pla_autre][1] * -G) / (((liste_p[t][pla_autre][0] - liste_p[t][planete_propre][0]) ** 2) + ((liste_p[t][pla_autre][1] - liste_p[t][planete_propre][1]) ** 2))
        
        liste_a.append(liste_acc_vide)
        
    return liste_p[temps]




plt.ion()

# Create a figure
fig = plt.figure()

# Create an empty list to hold the plot lines for each celestial body
lines = []

# Define the colors for each celestial body
colors = ['yellow', 'beige', 'orange', 'blue', 'red', 'brown', 'turquoise', 'lightblue', 'blue']

# Plot the Sun separately with a label
sun_line, = plt.plot([], [], marker='o', color=colors[0], label='Sun')
lines.append(sun_line)

# Loop through the desired time steps
for i in range(50):
    # Get the positions at the current time step
    positions = pop(i)

    # Clear the figure
    fig.clf()

    # Plot the positions for each celestial body
    for j, position in enumerate(positions):
        x_pos = position[0]
        y_pos = position[1]
        color = colors[j]  # Assign colors based on the index
        line, = plt.plot(x_pos, y_pos, marker='o', color=color, label=x[j][0])
        lines.append(line)

    # Set the x-axis and y-axis limits
    plt.xlim(-5e12, 5e12)
    plt.ylim(-5e12, 5e12)

    # Add legend
    plt.legend()

    # Update the plot
    fig.canvas.draw()

    # Pause for a short interval
    plt.pause(0.001)

    # Remove the plot lines
    for line in lines:
        line.remove()
    lines = []

# Turn off interactive mode


# Show the final plot
plt.show()
