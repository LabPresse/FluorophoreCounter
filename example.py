
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from fluorophore_counter import FluorophoreCounter


# Set parameters (modify these three lines as needed)
data = np.genfromtxt('data/example1.csv', delimiter=',')
fig, ax = plt.subplots(1, 1)
plt.ion()
plt.show()
ax.plot(data[0, :])
gain = None
brightness_guess = None
parameters = {
    'gain': gain,
    'flor_brightness_guess': brightness_guess,
    'num_states': 3,
}

# Run gibbs sampler
counter = FluorophoreCounter()
counter.gibbs_sampler(
    data=data,
    parameters=parameters,
    num_iter=100,
    save_name='my_data',
    plot_status=True,
)

# Get output
map_num_flors = counter.history.get('map').num_flors

# Done
print('Done! The number of fluorophores is: ', map_num_flors)
