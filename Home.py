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

def star_adjacency_matrix(n):
    # Create an empty adjacency matrix of size (n+1) x (n+1)
    adj_matrix = np.zeros((n+1, n+1), dtype=int)
    
    # Connect the central vertex (vertex 0) to all other vertices
    for i in range(1, n+1):
        adj_matrix[0, i] = 1
        adj_matrix[i, 0] = 1

    
    return adj_matrix


def adjacency_matrix_cycle(n):
    # Initialize an n x n matrix of zeros
    adj_matrix = np.zeros((n, n), dtype=int)
    
    # For a cycle, connect each node to the next, and the last to the first
    for i in range(n):
        adj_matrix[i, (i + 1) % n] = 1  # Connect to the next node (circular)
        adj_matrix[(i + 1) % n, i] = 1  # Ensure the graph is undirected
    
    return adj_matrix


dyn = lhc.DynRandomiser(dy.random_walk_noise, dy.lighthouses)
runner = lhc.Runner(star_adjacency_matrix(500),dyn)
data = runner.run_n_steps(n = 10000)

# stat.pdf_scaled_edges_plot(data, save_to_pdf= True)

stat.max_dif_dynamics_plot(data)