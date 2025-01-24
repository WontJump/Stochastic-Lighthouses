
from typing import Any
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages


def scaled_edges_plot(data, k):
    # Extract t values (keys)
    t_values = list(data.keys())

    # Extract y values (vectors) and identify the number of components
    y_values = list(data.values())

    # Determine the number of components in each vector (assuming all vectors are of the same length)
    num_components = len(y_values[0])

    # Plot each component of the vector separately
    for i in range(num_components):
        # Extract the i-th component of each vector
        y_component = [(1/k)*y[i] for y in y_values]
        plt.plot(t_values, y_component, label=f'Component {i + 1}')

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


def alt_scaled_edges_plot(data, k, components=None):
    # Extract t values (keys)
    t_values = list(data.keys())

    # Extract y values (vectors)
    y_values = list(data.values())

    # Determine the number of components in each vector (assuming all vectors are of the same length)
    num_components = len(y_values[0])

    # If components is None, plot all components, otherwise filter by the specified components
    if components is None:
        components = range(num_components)  # Default to all components

    # Plot each specified component of the vector separately
    for i in components:
        # Extract the i-th component of each vector
        y_component = [(1/k) * y[i] for y in y_values]
        plt.plot(t_values, y_component, label=f'Component {i + 1}')

    # Label the axes
    plt.xlabel('t')  # x-axis label
    plt.ylabel('y')  # y-axis label

    # Title of the plot
    plt.title('Line Plot of Selected Vector Components vs. t')

    # Show legend
    plt.legend()

    # Show the plot
    plt.show()


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


def sum_scaled_dynamics_plot(data, k):
    t_values = list(data.keys())
    y_values = list(data.values())
    y_values = [(1/k)*np.sum(i) for i in y_values]

    # Create a line plot
    plt.plot(t_values, y_values)

    # Label the axes
    plt.xlabel('t')  # x-axis label (Independent variable)
    plt.ylabel('y')  # y-axis label (Dependent variable)

    # Title of the plot
    plt.title('scaled Line Plot of y vs. t')

    # Show the plot
    plt.show() 
    pass

def absolute_scaled_sum_plot(data,k): 
    t_values = list(data.keys())
    y_values = list(data.values())
    y_values = [(1/k)*np.sum(np.abs(i)) for i in y_values]

    # Create a line plot
    plt.plot(t_values, y_values)

    # Label the axes
    plt.xlabel('t')  # x-axis label (Independent variable)
    plt.ylabel('y')  # y-axis label (Dependent variable)

    # Title of the plot
    plt.title('Scalded absolute Line Plot of y vs. t')

    # Show the plot
    plt.show() 
    pass   


# I don't think you should scale the individual compoenets in this case as we aren't really averaging them 
def pdf_scaled_edges_plot(data, components=None, save_to_pdf=False, pdf_filename="components_plot.pdf"):
    # Extract t values (keys)
    t_values = list(data.keys())

    # Extract y values (vectors)
    y_values = list(data.values())

    # Determine the number of components in each vector (assuming all vectors are of the same length)
    num_components = len(y_values[0])

    # If components is None, plot all components, otherwise filter by the specified components
    if components is None:
        components = range(num_components)  # Default to all components

    # If save_to_pdf is True, create a PdfPages object
    if save_to_pdf:
        pdf_pages = PdfPages(pdf_filename)

    # Plot each specified component of the vector separately
    for i in components:
        # Extract the i-th component of each vector
        y_component = [y[i] for y in y_values]
        
        # Create a new figure for each component
        plt.figure(figsize=(40, 6))  # Set figure size (adjust width and height)

        # Plot the component
        plt.plot(t_values, y_component, label=f'Component {i + 1}')

        # Label the axes
        plt.xlabel('t')  # x-axis label
        plt.ylabel('y')  # y-axis label

        # Title of the plot
        plt.title(f'Line Plot of Component {i + 1} vs. t')

        # Show legend
        plt.legend()

        # If saving to PDF, save the plot to the pdf file
        if save_to_pdf:
            pdf_pages.savefig()  # Save the current figure to the PDF
        else:
            plt.show()  # Show the plot interactively

        # Close the current figure to avoid overlapping plots
        plt.close()

    # Close the PDF if we're saving to it
    if save_to_pdf:
        pdf_pages.close()


def max_dif_dynamics_plot(data):
    t_values = list(data.keys())
    y_values = list(data.values())
    y_values = [np.max(i) - np.min(i) for i in y_values]

    # Create a line plot
    plt.plot(t_values, y_values)

    # Label the axes
    plt.xlabel('t')  # x-axis label (Independent variable)
    plt.ylabel('y')  # y-axis label (Dependent variable)

    # Title of the plot
    plt.title('max diff Plot of y vs. t')

    # Show the plot
    plt.show() 
    pass
