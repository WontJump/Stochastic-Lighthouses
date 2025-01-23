import dynamics as dy 
import lightHouseClasses as lhc
import statistics_1 as stat
import numpy as np


adj = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])

# Create a 10x10 matrix filled with ones
def completeAdj(n):
    adjacency_matrix = np.ones((n, n))
    np.fill_diagonal(adjacency_matrix, 0)
    return adjacency_matrix

import numpy as np

def adjChain(n):
    # Create a square matrix of size n x n, initialized with zeros
    adj_matrix = np.zeros((n, n), dtype=int)
    
    # Set the adjacent vertices (edges in the chain)
    for i in range(n - 1):
        adj_matrix[i, i+1] = 1
        adj_matrix[i+1, i] = 1
    
    return adj_matrix



dyn = lhc.DynRandomiser(dy.random_walk_noise, dy.lighthouses)
runner = lhc.Runner(adjChain(50),dyn)
data = runner.run_n_steps(n = 100000)

stat.sum_scaled_dynamics_plot(data, k = 50)
