def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    result = []
    for i in image:
        color = []
        for j in i:
            
            c = j[0]*0.299 + j[1]*0.587 + j[2]*0.114
            color.append(c)
        result.append(color)
    return result