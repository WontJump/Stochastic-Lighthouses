from typing import Any
import numpy as np
import matplotlib.pyplot as plt
# runner store vertex vars store data and initiate dynamics on variables
# dynamic takes the variables and then gives updated variables. 


class Runner:
    def __init__(self, adj, dyn): 
        shape = adj.shape
        dim = shape[0]

        self.dyn_vars = np.zeros(dim) # this assums that adj is a numpy array 
        self.dyn_hist = {} 
        self.dyn = dyn
        self.dyn.set_adj(adj)
        pass
    
    def run_n_steps(self, start = None, n = 10): 
        if start: 
            self.dyn_vars = start # should also add in some type checking here 
        self.dyn_hist[0] = self.dyn_vars
        # note that at the moment the history is not reset in anyway. THis might be a problem 
        for i in range(n): 
            print('lhc' , self.dyn_vars)

            # self.dyn_vars = self.dyn(self.dyn_vars)
            x = self.dyn(self.dyn_vars)
            print('lhc ?' , x)
            self.dyn_hist[i] = self.dyn_vars
            
        return self.dyn_hist
    
class DynRandomiser: 
    # the reason this class exists is to combine a structural dynamic with a particular kind of randomness. i.e if we want to replace a bernoulli 
    # random variable with normal without having to re- code everything. So we also need functions which take randomness and adjacency as argumetns
    def __init__(self,noise, dyn):
        self.rand = noise # idea is this function takes either takes a vector and adds our randomness to it or takes an individual edge and adds randomness to it 
        self.dynamic = dyn
        self.adj = 'unset'

    def set_adj(self, Adj): 
        self.adj = Adj

 
    def __call__(self, var):  # this is the thing I want to make into a lambda function thingy 
    # i.e I need it to be able to set Adj forever with a single call?
        self.dynamic(self.adj,self.rand, var)
