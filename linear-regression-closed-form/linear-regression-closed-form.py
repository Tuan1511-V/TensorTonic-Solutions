import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X_T = np.array(X).T
    X = np.array(X)
    y = np.array(y)
    p = X_T@X
    p = np.linalg.inv(p)
    v = X_T@y
    w = p@v
    return w