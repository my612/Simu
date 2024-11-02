from matplotlib import pyplot as plt
import numpy as np
from utils.reading import parseSimFile

# Function to plot the waveform
def waveform(simPath, inputs, outputs): 
    data = parseSimFile(simPath, inputs, outputs) # Parsing the simulation file
    maxTime = 0
    keysLen = data.keys().__len__()  # Getting the number of keys
    fig, ax = plt.subplots(keysLen, sharex=True, sharey=True) # Creating the subplots
    fig.set_layout_engine("constrained") # Setting the layout engine
    fig.subplots_adjust(left=2, right=2, top=2, bottom=2) 
    for i, key in enumerate(data.keys()): # Iterating through the keys to plot the waveforms for each key
        x_values, y_values = zip(*[(int(x), int(y)) for x, y in data[key]]) # Getting the x and y values
        maxTime = max(maxTime, max(x_values)) # Getting the maximum time
        x_values = list(x_values) + [maxTime, maxTime * 1.5] # Adding the maximum time to the x values
        y_values = list(y_values) + [y_values[-1], y_values[-1]] # Adding the last y value to the y values
        ax[i].step(x_values, y_values, where="post") # Plotting the step graph
        ax[i].text( # Adding the text to the graph
            -0.1,
            0.5,
            key,
            transform=ax[i].transAxes,
            fontsize=12,
            va="center",
            ha="right",
        )
    plt.yticks([0, 1])  # Setting the y ticks
    plt.xticks(np.arange(0, maxTime * 1.5, step=100)) # Setting the x ticks
    fig.set_size_inches(maxTime * 2 / 300, 10) # Setting the size of the figure
    plt.show() 
