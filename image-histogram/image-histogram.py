def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    hist = [0 for _ in range(256)]
    count = {}
    for i in image:
        for j in i:
            if j in count:
                count[j] +=1
            else:
                count[j] = 1
            hist[j] = count[j]
    return hist