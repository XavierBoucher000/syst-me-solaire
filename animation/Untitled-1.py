import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pickle

loaded_result = np.load('result.npy')



cut_list = loaded_result[::3600*24]

# Cut down the list to keep every 3600th element and its multiples


import matplotlib.pyplot as plt

# Enable interactive mode
plt.ion()

# Create a figure with black background
fig = plt.figure(facecolor='black')

# Define colors and labels
colors = ['yellow','black', 'orange', 'blue', 'red', 'brown', 'turquoise', 'lightblue', 'blue']
labels = ['Soleil','Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune']

# Loop through the positions
for data in cut_list:
    # Clear the current plot
    plt.clf()

    # Loop through the sublists (sun and planets)
    for i, pos in enumerate(data):
        # Extract x and y coordinates
        x_pos = pos[0]
        y_pos = pos[1]

        # Get the color and label
        color = colors[i % len(colors)]
        label = labels[i] if i < len(labels) else f'Planet {i+1}'

        # Plot the position
        plt.scatter(x_pos, y_pos, marker='o', color=color, label=label)

    # Set the x-axis and y-axis limits
    plt.xlim(-8e11, 8e11)
    plt.ylim(-8e11, 8e11)

    # Add legend
    plt.legend()

    # Update the plot
    plt.draw()
    plt.pause(0.01)

# Turn off interactive mode
plt.ioff()

# Show the final plot
plt.show()
