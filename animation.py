
import matplotlib.pyplot as plt
import numpy as np

loaded_result = np.load('result.npy')
cut_list = loaded_result[::3000]
print(cut_list)
# Enable interactive mode
plt.ion()

# Set the dark background style
plt.style.use('dark_background')

# Create a figure with black background
fig = plt.figure(facecolor='black')

# Define colors and labels
colors = ['#FDB813', '#B89C74', 'orange', '#0052A5', 'red', '#D7A558', '#C18F5A', '#00CED1', '#1E90FF']
labels = ['Soleil', 'Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune']

# Define scaling factors for point sizes
sun_scaling_factor = 100.0
planet_scaling_factor = 20.0
small_planet_scaling_factor = 15.0
mars_scaling_factor = 10.0
jupiter_scaling_factor = 50.0
saturn_scaling_factor = 40.0
uranus_scaling_factor = 30.0
neptune_scaling_factor = 30.0

# Initialize previous positions
prev_positions = [[[], []] for _ in range(len(labels))]

# Plot smaller planets first
for data in cut_list:
    # Clear the current plot
    plt.clf()

    # Plot smaller planets
    for i, pos in enumerate(data):
        # Exclude larger planets and Sun
        if i in [5, 6, 7, 8]:  # Exclude Jupiter, Saturn, Uranus, Neptune
            continue

        # Extract x and y coordinates
        x_pos = pos[0]
        y_pos = pos[1]

        # Get the color and label
        color = colors[i % len(colors)]
        label = labels[i] if i < len(labels) else f'Planet {i+1}'

        # Determine the scaling factor based on the label
        if label == 'Soleil':
            size = sun_scaling_factor
        else:
            size = small_planet_scaling_factor

        # Plot the position
        plt.scatter(x_pos, y_pos, marker='o', color=color, label=label, s=size)

        # Update orbit
        prev_positions[i][0].append(x_pos)
        prev_positions[i][1].append(y_pos)
        plt.plot(prev_positions[i][0], prev_positions[i][1], color=color, alpha=0.3)

    # Set the x-axis and y-axis limits for smaller planets
    plt.xlim(-8e11, 8e11)
    plt.ylim(-8e11, 8e11)
    plt.gca().set_aspect('equal')

    # Add legend for smaller planets
    plt.legend(loc='upper left')

    # Update the plot
    plt.draw()
    plt.pause(0.01)

# Clear the plot
plt.clf()

# Plot larger planets and Sun only
for data in cut_list:
    # Clear the current plot
    plt.clf()

    # Plot larger planets and Sun
    for i, pos in enumerate(data):
        # Exclude smaller planets
        if i in [1, 2, 3, 4]:  # Exclude Mercury, Venus, Earth, Mars
            continue

        # Extract x and y coordinates
        x_pos = pos[0]
        y_pos = pos[1]

        # Get the color and label
        color = colors[i % len(colors)]
        label = labels[i] if i < len(labels) else f'Planet {i+1}'

        # Determine the scaling factor based on the label
        if label == 'Soleil':
            size = sun_scaling_factor
        elif label == 'Jupiter':
            size = jupiter_scaling_factor
        elif label == 'Saturne':
            size = saturn_scaling_factor
        elif label == 'Uranus':
            size = uranus_scaling_factor
        elif label == 'Neptune':
            size = neptune_scaling_factor
        else:
            size = planet_scaling_factor

        # Plot the position
        plt.scatter(x_pos, y_pos, marker='o', color=color, label=label, s=size)

        # Update orbit
        prev_positions[i][0].append(x_pos)
        prev_positions[i][1].append(y_pos)
        plt.plot(prev_positions[i][0], prev_positions[i][1], color=color, alpha=0.3)

    # Set the x-axis and y-axis limits for larger planets
    plt.xlim(-4.6e12, 4.6e12)
    plt.ylim(-4.6e12, 4.6e12)
    plt.gca().set_aspect('equal')

    # Add legend for larger planets
    plt.legend(loc='upper left')

    # Update the plot
    plt.draw()
    plt.pause(0.01)

# Turn off interactive mode
plt.ioff()

# Show the final plot
plt.show()
