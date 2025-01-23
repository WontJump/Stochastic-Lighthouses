import dynamics as dy 
import lightHouseClasses as lhc
import statistics_1 as stat
import numpy as np


adj = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
])



dyn = lhc.DynRandomiser(dy.random_walk_noise, dy.lighthouses)
runner = lhc.Runner(adj,dyn)
print(runner.run_n_steps())


