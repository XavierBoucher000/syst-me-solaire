import matplotlib.pyplot as plt
import numpy as np

loaded_result = np.load('result.npy')
astres_names = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Moon"]
max_magnitudes = [float('-inf')] * 10
min_magnitudes = [float('inf')] * 10
ex = [0] * 10

for t in range(60 * 24 * 30):
    for astres in range(10):
        magnitude = np.sqrt(loaded_result[t][astres][0]**2 + loaded_result[t][astres][1]**2)
        if magnitude > max_magnitudes[astres]:
            max_magnitudes[astres] = magnitude
        if magnitude < min_magnitudes[astres]:
            min_magnitudes[astres] = magnitude

for astres in range(10):
    ex[astres] = (max_magnitudes[astres] - min_magnitudes[astres]) / (max_magnitudes[astres] + min_magnitudes[astres])
    print("Planet:", astres_names[astres])
    print("Max Magnitude:", max_magnitudes[astres])
    print("Min Magnitude:", min_magnitudes[astres])
    print("Eccentricity (ex):", ex[astres])
    print()


cut_list = loaded_result[::300]

# Enable interactive mode
plt.ion()

# Set the dark background style
plt.style.use('dark_background')

# Create a figure with black background
fig = plt.figure(facecolor='black')

# Define colors and labels
colors = ['#FDB813', '#B89C74', 'orange', '#0052A5', 'red', '#D7A558', '#C18F5A', '#00CED1', '#1E90FF', 'white', 'yellow']
labels = ['Soleil', 'Mercure', 'Venus', 'Terre', 'Mars', 'Jupiter', 'Saturne', 'Uranus', 'Neptune', 'Lune', 'Io']

# Define scaling factors for point sizes
sun_scaling_factor = 100.0
planet_scaling_factor = 20.0
small_planet_scaling_factor = 15.0
mars_scaling_factor = 10.0
jupiter_scaling_factor = 50.0
saturn_scaling_factor = 40.0
uranus_scaling_factor = 30.0
neptune_scaling_factor = 30.0
moon_scaling_factor = 5.0
io_scaling_factor = 5.0

prev_positions = [[[], []] for _ in range(len(labels))]

# Plot Moon, Earth, and Sun
for data in cut_list:
    # Clear the current plot
    plt.clf()

    # Plot Moon, Earth, and Sun
    for i, pos in enumerate(data):
        # Exclude other planets and moons
        if i not in [3, 9, 0]:  # Earth, Moon, Sun
            continue

        # Extract x and y coordinates
        x_pos = pos[0]
        y_pos = pos[1]

        # Get the color and label
        color = colors[i % len(colors)]
        label = labels[i] if i < len(labels) else f'Planet {i+1}'

        # Determine the scaling factor based on the label
        if label == 'Soleil':
            size = 100.0  # Sun scaling factor
        elif label == 'Lune':
            size = 10.0  # Moon scaling factor
        else:
            size = 30.0  # Earth scaling factor

        # Plot the position
        plt.scatter(x_pos, y_pos, marker='o', color=color, label=label, s=size)

        # Update orbit
        prev_positions[i][0].append(x_pos)
        prev_positions[i][1].append(y_pos)
        plt.plot(prev_positions[i][0], prev_positions[i][1], color=color, alpha=0.3)

    # Set the x-axis and y-axis limits
    plt.xlim(-1.6e11, 1.6e11)  # Adjust the limits as needed
    plt.ylim(-1.6e11, 1.6e11)  # Adjust the limits as needed
    plt.gca().set_aspect('equal')

    # Add legend
    plt.legend(loc='upper left')

    # Update the plot
    plt.draw()
    plt.pause(0.01)
# Initialize previous positions
prev_positions = [[[], []] for _ in range(len(labels))]

# Plot smaller planets first
for data in cut_list:
    # Clear the current plot
    plt.clf()

    # Plot smaller planets
    for i, pos in enumerate(data):
        # Exclude larger planets, Sun, and Io from the smaller planets
        if i in [5, 6, 7, 8, 10]:  # Exclude Jupiter, Saturn, Uranus, Neptune, Io
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
        elif label == 'Lune':
            size = moon_scaling_factor
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
        # Exclude smaller planets and Moon from the larger planets
        if i in [1, 2, 3, 4, 9]:  # Exclude Mercury, Venus, Earth, Mars, Moon
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
        elif label == 'Io':
            size = io_scaling_factor
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
