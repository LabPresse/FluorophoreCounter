
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from fluorophore_counter import FluorophoreCounter

# Set parameters (modify these lines as needed)
data = np.genfromtxt('data/example2.csv', delimiter=',')

# Set parameters
parameters = {
    'gain': 2,                     # Camera gain (use 2 when unknown)
    'flor_brightness_guess': 200,  # Look at the data and estimate the step hight
    'num_states': 4,               # 4 states: Bright, Dim, Blink, Bleached
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

# Plot
counter.plot_variables(roi=[0, 1, 2])

# Done
print('Done! The number of fluorophores is: ', map_num_flor)
