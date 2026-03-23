def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    
    H = len(image)
    W = len(image[0])
    k = len(kernel)
    s = stride
    H_out = (H+2*padding-k)//stride + 1
    W_out = (W+2*padding-k)//stride + 1
    H_pad = H + 2*padding
    W_pad = W + 2*padding
    pad_img = [[0 for _ in range(W_pad)] for _ in range(H_pad)]

    for j in range(H):
        for i in range(W):
            new_j = j + padding
            new_i = i + padding
            pad_img[new_j][new_i] = image[j][i]
    # pad_img = np.array(pad_img)
    # kernel = np.array(kernel)
    output = [[0 for _ in range(W_out)] for _ in range(H_out)]

    for j in range(H_out):
        for i in range(W_out):
            sum = 0
            for m in range(len(kernel)):
                for n in range(len(kernel[0])):
                    sum += pad_img[j*s+n][i*s+m]*kernel[m][n]
            output[j][i] = sum
    return output
            
    