
from typing import Any
import numpy as np
import matplotlib.pyplot as plt

def all_edges_plot(data):
    # Extract t values (keys)
    t_values = list(data.keys())

    # Extract y values (vectors) and identify the number of components
    y_values = list(data.values())

    # Determine the number of components in each vector (assuming all vectors are of the same length)
    num_components = len(y_values[0])

    # Plot each component of the vector separately
    for i in range(num_components):
        # Extract the i-th component of each vector
        y_component = [y[i] for y in y_values]
        plt.plot(t_values, y_component, marker='o', label=f'Component {i + 1}')

    # Label the axes
    plt.xlabel('t')  # x-axis label
    plt.ylabel('y')  # y-axis label

    # Title of the plot
    plt.title('Line Plot of Vector Components vs. t')

    # Show legend
    plt.legend()

    # Show the plot
    plt.show()     
    pass

def sum_of_all_dynamics_plot(data):
    t_values = list(data.keys())
    y_values = list(data.values())
    y_values = [np.sum(i) for i in y_values]

    # Create a line plot
    plt.plot(t_values, y_values, marker='o')

    # Label the axes
    plt.xlabel('t')  # x-axis label (Independent variable)
    plt.ylabel('y')  # y-axis label (Dependent variable)

    # Title of the plot
    plt.title('Line Plot of y vs. t')

    # Show the plot
    plt.show() 
    pass

def absolute_sum_plot(data): 
    t_values = list(data.keys())
    y_values = list(data.values())
    y_values = [np.sum(np.abs(i)) for i in y_values]

    # Create a line plot
    plt.plot(t_values, y_values, marker='o')

    # Label the axes
    plt.xlabel('t')  # x-axis label (Independent variable)
    plt.ylabel('y')  # y-axis label (Dependent variable)

    # Title of the plot
    plt.title('Line Plot of y vs. t')

    # Show the plot
    plt.show() 
    pass   
