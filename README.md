# Solar System Simulation

This repository contains a Python code for simulating the motion of celestial bodies in the solar system using basic physics principles.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git

2. Install the required dependencies:

pip install numpy matplotlib

## Usage

The main simulation is implemented in the pop() function, which calculates the positions of the planets in the solar system over a given time period. The function takes a single argument, temps, representing the duration of the simulation in seconds.

result = pop(3600*24*45)

The pop() function returns a list of positions for each planet at different time intervals.

To visualize the simulation, you can use the provided animation function. The animation function takes the simulation results and creates an animated plot using the matplotlib library.

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(result):
    # Create an animation plot using the simulation results
    fig = plt.figure()
    ax = plt.axes(xlim=(-5e12, 5e12), ylim=(-5e12, 5e12))
    line, = ax.plot([], [], 'o')

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        x = [pos[0] for pos in result[frame]]
        y = [pos[1] for pos in result[frame]]
        line.set_data(x, y)
        return line,

    anim = animation.FuncAnimation(fig, update, frames=len(result), init_func=init, blit=True)
    plt.show()

animate(result)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://opensource.org/licenses/MIT)