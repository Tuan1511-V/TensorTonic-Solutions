def morphological_op(image, kernel, operation):
    """
    Áp dụng phép mòn (erosion) hoặc nở (dilation) cho ảnh nhị phân.
    """
    h_k = len(kernel)
    w_k = len(kernel[0])
    H = len(image)
    W = len(image[0])
    
    pad_h = h_k // 2
    pad_w = w_k // 2
    
   
    H_pad = H + 2 * pad_h
    W_pad = W + 2 * pad_w
    img_pad = [[0 for _ in range(W_pad)] for _ in range(H_pad)]
    
    for j in range(H):
        for i in range(W):
            img_pad[j + pad_h][i + pad_w] = image[j][i]
            
    res = [[0 for _ in range(W)] for _ in range(H)]
    
    if operation == "dilate":
        for j in range(H):
            for i in range(W):
                found = False
                for m in range(h_k):
                    for n in range(w_k):
                        if kernel[m][n] == 1 and img_pad[j + m][i + n] == 1:
                            found = True
                            break
                    if found: break
                res[j][i] = 1 if found else 0
                
    elif operation == "erode":
        for j in range(H):
            for i in range(W):
                match = True
                for m in range(h_k):
                    for n in range(w_k):
                        if kernel[m][n] == 1 and img_pad[j + m][i + n] == 0:
                            match = False
                            break
                    if not match: break
                res[j][i] = 1 if match else 0
                
    return res