# A simple graph Dynamic simulation 

This is the classic discrete heat equation on a graph with a slight twist. When each node tries to take an average of its neibours it gets it wrong (introducing a random variable for each neibour). This means the plots produced by this code look very brownian. In general they aren't (I believe) but we can easily show they're Levy Processes with distributions we can determine Numerically or CLT (depending on taste).
