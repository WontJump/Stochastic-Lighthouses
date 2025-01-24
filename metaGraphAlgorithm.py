#Idea for each component consider each pair, take the difference then absolute sum, take the inverse and assign to a meta graph 
# then do a vertex clustering alagorithm? 

import itertools 
import numpy as np 
import networkx as nx 

def get_pairs(lst):
    return list(itertools.combinations(lst, 2))

# this doesn't work yet! it needs to also take another argument... I don't know which one byt I know I'm treating the indexes like 
# theyre vectors which is obviouslt wrong 
def abs_difference_store(lst):
    # note we take the inverse inside this function! 
    # also 10000 is used as a default value inside this function! 
    dif_dict = {} 
    for i,j in get_pairs(lst): 
        dif = i - j 
        dif = np.sum(np.abs(dif)) 
        if dif: 
            dif_dict[(i,j)] = 1/dif 
        else: 
           dif_dict[(i,j)] = 10000 #this should be an arbitarily high number   
    return dif_dict 
    



# Add edges with weights from the dictionary

for (i, j), weight in edges_dict.items():
    G.add_edge(i, j, weight=weight)

def path_dif_graph(lst): 
    G = nx.Graph()
    dif_dict = abs_difference_store(lst)
    for (i, j), weight in dif_dict.items():
        G.add_edge(i, j, weight=weight)
    
    return G 


def louvain_clustering_of_noise(lst): 
    return nx.louvain_communities(path_dif_graph(lst))
    