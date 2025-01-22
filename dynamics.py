import numpy as np 

# now I'm going to code up the example function which I want to try and apply. 

# sadly I think this is destined to be inneficient so I;m just going to roll with the punches 

def lighthouses(Adj, noise,  var_t1): 
    var_t2 =np.zeros(var_t1.shape) 

    print(var_t2)

    for i in range(var_t1.shape[0]): 
        column_i = Adj[:, i]
        dot_product = np.dot(column_i, noise(var_t1))
        degree = np.sum(column_i) 
        var_t2[i] = 1/degree * dot_product 
    
    print(var_t2)
    # return var_t2
    return 1

def random_walk_noise(var): 
    dim = var.shape[0]
    return var + np.random.choice([-1, 1], size= dim) # hopefully this will give the right type of noise 

