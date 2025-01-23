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
data = runner.run_n_steps(n = 100000)

stat.sum_of_all_dynamics_plot(data)
