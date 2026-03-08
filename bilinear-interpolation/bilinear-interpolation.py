def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    H = len(image)
    W = len(image[0])
    h_ratio = (H - 1) / (new_h - 1) if new_h > 1 else 0
    w_ratio = (W - 1) / (new_w - 1) if new_w > 1 else 0
    
    output = []
    for i in range(new_h):
        out = []
        for j in range(new_w):
            src_y = i * h_ratio
            src_x = j * w_ratio
            
            y_0 = int(src_y)
            x_0 = int(src_x)
            y_1 = min(y_0+1,H-1)
            x_1 = min(x_0+1,W-1)
            
            dy = src_y - y_0
            dx = src_x - x_0

            interpol_val  = image[y_0][x_0]*(1-dy)*(1-dx) + image[y_1][x_0]*dy*(1-dx) + image[y_0][x_1]*(1-dy)*dx + image[y_1][x_1]*dy*dx
            out.append(interpol_val)
        output.append(out)
    return output
            