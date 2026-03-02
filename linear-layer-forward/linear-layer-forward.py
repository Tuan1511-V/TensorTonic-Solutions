def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    X = np.array(X)
    W = np.array(W)
    b = np.array(b)
    result = np.matmul(X,W) + b
    return result.tolist()