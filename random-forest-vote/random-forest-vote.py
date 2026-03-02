import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions = np.array(predictions).T
    pred = []
    # if len(predictions) == 1:
    #     for predict in predictions:
    #         pred = predict
    if len(predictions) > 1:
        for predict in predictions:
            f = {}
            for i in predict:
                # f[i] = f.get(i,0)+1
                if (i in f):
                    f[i] +=1
                elif (i not in f):
                    f[i] = 1
            v = max(f.values())    
            p = [k for k in f if f[k] == v]
            pred.append(min(p))
            # if (p):
            # pred.append(max(sorted(f), key=f.get))
            # else:
            #     pred.append(min(f,key=f.get))

        return pred
    return predictions[0]
        