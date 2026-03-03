def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride = image_size/feature_size
    center = []
    
    a_boxes = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j+0.5)*stride
            cy = (i+0.5)*stride
            # t = (cx,cy)
            # center.append(t)
            for s in scales:
                for r in aspect_ratios:
                    w = s*math.sqrt(r)
                    h = s / math.sqrt(r)
                    a = [cx - w/2, cy - h/2, cx + w/2, cy + h/2]
                    a_boxes.append(a)
    
   
    # for c in center:
    #     a = [c[0]-w/2, c[1]-h/2, cx+w/2,cy+h/2]
    #     a_boxes.append(a)
    return a_boxes