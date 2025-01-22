from typing import Any
import numpy as np
import matplotlib.pyplot as plt
# runner store vertex vars store data and initiate dynamics on variables
# dynamic takes the variables and then gives updated variables. 

# class Test: 
#     def __init__(self, text) -> None:
#         self.text = text

#     def text_to_say(self, stuff): 
#         print(stuff, self.text)
#         pass

# T = Test('hi') 

# T.text_to_say('biotch')

class Runner:
    def __init__(self, adj, dyn): 

        self.dyn_vars = np.zeros(adj.shape()[0]) # this assums that adj is a numpy array 
        self.dyn_hist = {} 
        self.dyn = dyn(adj)
        pass
    
    def run_n_steps(self, start = None, n = 10): 
        if not start: 
            self.dyn_var = start # should also add in some type checking here 
        self.dyn_hist[0] = self.dyn_var  
        # note that at the moment the history is not reset in anyway. THis might be a problem 
        for i in range(n): 

            self.dyn_var = self.dyn(self.dyn_var)
            self.dyn_hist[i] = self.dyn_vars
            
        return self.dyn_hist
    
class Dyn: 
    # the reason this class exists is to combine a structural dynamic with a particular kind of randomness. i.e if we want to replace a bernoulli 
    # random variable with normal without having to re- code everything. So we also need functions which take randomness and adjacency as argumetns
    def __init__(self, Rand, actual_thing):
        self.rand = Rand # idea is this function takes either takes a vector and adds our randomness to it or takes an individual edge and adds randomness to it 
        self.dynamic = actual_thing
    def __call__(self, Adj):  # this is the thing I want to make into a lambda function thingy 
    # i.e I need it to be able to set Adj forever with a single call?
        self.dynamic(Adj,)

# now I'm going to code up the example function which I want to try and apply. 

# sadly I think this is destined to be inneficient so I;m just going to roll with the punches 

def lighthouses(Adj, noise,  var_t1): 
    var_t2 =np.zeros(var_t1.shape()) 

    for i in range(var_t1.shape()[0]): 
        column_i = Adj[:, i]
        dot_product = np.dot(column_i, noise(var_t1))
        degree = np.sum(column_i) 
        var_t2[i] = 1/degree * dot_product 
    
    return var_t2








-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



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
