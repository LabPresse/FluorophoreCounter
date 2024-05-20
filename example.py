
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from fluorophore_counter import FluorophoreCounter

data1 = [3,5,4,3,3,5,15,6,6,5]
data2 = [183,133,120,105,116,97,99,87,92,120,144]

# Histogram
fig, ax = plt.subplots(1, 1)
plt.ion()
plt.show()
ax.hist(data1, bins=10, alpha=0.5, label='data1')
ax.hist(data2, bins=10, alpha=0.5, label='data2')
plt.pause(1)

# Set parameters (modify these three lines as needed)
data = np.genfromtxt('data/example2.csv', delimiter=',')
gain = 2
brightness_guess = 100
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
map_num_flor = counter.history.get('map').num_flor

# Done
print('Done! The number of fluorophores is: ', map_num_flor)
