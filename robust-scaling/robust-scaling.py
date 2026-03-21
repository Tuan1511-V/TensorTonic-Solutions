def robust_scaling(values):
    """
    Scale proc using median and interquartile range.
    """
    proc = sorted(values)
    n = len(proc)
    if n == 1:
        return [0.0]
    if n%2 == 0:
        med = (proc[n//2]+proc[n//2-1])/2
        first = proc[:n//2]
        third = proc[n//2:]
    else:
        med = proc[n//2]
        first = proc[:n//2]
        third = proc[n//2+1:]
    
    
   
    m = len(first)
    k = len(third)

    if m > 0 and k > 0:
        if m % 2 == 0:
            q1 = (first[m // 2] + first[m // 2 - 1]) / 2
        else:
            q1 = first[m // 2]
            
        if k % 2 == 0:
            q3 = (third[k // 2] + third[k // 2 - 1]) / 2
        else:
            q3 = third[k // 2]
    iqr = [(i-med)/(q3-q1) for i in values if(q3-q1>0)]
    if q3-q1 == 0:
        return [i-med for i in values]
    return iqr