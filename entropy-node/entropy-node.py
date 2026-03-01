import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if not y:
        return 0.0
    x = []
    for i in y:
        if (i not in x):
            x.append(i)
    
        
    sum = 0
    for a in range(len(x)):
        p = y.count(x[a])/len(y)
        if p>0:
            sum+= p*np.log2(p)
        
    return -float(sum)
    