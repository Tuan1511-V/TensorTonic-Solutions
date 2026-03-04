import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # mean = total/len(X)
    # var = sum((i-mean)**2)/len(X)
    # norm = (i-mean)/sqrt(var+eps)
    # y_hat = gamma*norm_i+beta
    # total = 0
    # for i in x:
    #     total += i
    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    if x.ndim == 2:
        reduce_ax = 0
    elif x.ndim == 4:
        reduce_ax = 0,2,3
    mean = x.mean(axis=reduce_ax, keepdims = True)
    var = x.var(axis=reduce_ax, keepdims = True)
    if x.ndim == 4:
        gamma = gamma.reshape(1, -1, 1, 1) 
        beta = beta.reshape(1, -1, 1, 1)
    x_hat = (x-mean)/np.sqrt(var+eps)        
    y_hat = x_hat *gamma + beta
    return y_hat      