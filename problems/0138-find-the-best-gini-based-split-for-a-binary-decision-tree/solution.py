import numpy as np
from typing import Tuple

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    """Return the (feature_index, threshold) that minimises weighted Gini impurity."""
    # ✏️ TODO: implement
    pass
    i = 0
    lst = []
    gini_min = np.inf
    gini_thres  = 0
    gini_idx = 0
    best_feature = 0
    for c in range(X.shape[1]):
        sort_idx = np.argsort(X[:, c])
        x = X[:, c][sort_idx]
        y_s = y[sort_idx]
        x_new = np.unique(x)[:-1] 

        idx = 0
        for r in x_new:
            pr_true_1 = ((x<=r) & (y_s == 1)).sum()/ (x<=r).sum()
            pr_true_0 = 1 - pr_true_1
            gini_left = 1-pr_true_0**2 - pr_true_1**2
            pr_false_1 = ((x>r) & (y_s == 1)).sum()/ (x>r).sum()
            pr_false_0 = 1 -pr_false_1
            gini_right = 1-pr_false_1**2 - pr_false_0**2
            wl = (x<r).sum() / ((x<r).sum() + (x>r).sum())
            gini = wl*gini_left+(1-wl)*gini_right
            if gini<gini_min:
                gini_min = gini
                gini_thres = r
                gini_idx = idx
                best_feature = c
            idx = idx+1
        lst.append([gini_idx, gini_thres])
        i = i+1
    return(best_feature, gini_thres)

