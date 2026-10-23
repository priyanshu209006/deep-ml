import numpy as np

def entropy_split_selection(X: np.ndarray, y: np.ndarray) -> tuple:
    """
    Find the best feature and threshold for splitting based on information gain.
    
    Args:
        X: Feature matrix of shape (n_samples, n_features)
        y: Labels of shape (n_samples,)
    
    Returns:
        Tuple of (best_feature_index, best_threshold, best_info_gain)
    """
    # Your code here
    pass
    best_info_gain = -np.inf
    best_feature_index = 0
    best_threshold = 0

    classes, count = np.unique(y, return_counts=True)
    p_c = count / len(y)

    parent_entropy = np.sum(-p_c*(np.where(p_c!=0,np.log2(p_c),0)))
    for c in range(X.shape[1]):
        sort_idx = np.argsort(X[:, c])
        x = X[:, c][sort_idx]
        y_s = y[sort_idx]
        x_new = []
        for i in range((X.shape[0])-1):
            x_new.append((x[i]+x[i+1])/2)
        for k in range(len(x_new)):
            pr_c_left =[]
            pr_c_right = []
            for num in range(len(classes)):
                pr_c_left.append(np.sum((x<x_new[k]) & (y_s==classes[num]))/(np.sum(x<x_new[k]) if np.sum(x<x_new[k])!=0 else 1))
                pr_c_right.append(np.sum((x>x_new[k]) & (y_s==classes[num]))/(np.sum(x>x_new[k]) if np.sum(x>x_new[k])!=0 else 1))

            pr_l_ar = np.array(pr_c_left)
            pr_r_ar = np.array(pr_c_right)
            
            H_s_left = np.sum(-pr_l_ar*(np.where(pr_l_ar > 0, np.log2(pr_l_ar), 0)))
            H_s_right= np.sum(-pr_r_ar*(np.where(pr_r_ar > 0, np.log2(pr_r_ar), 0)))
            
            wl = np.sum(x<x_new[k])/len(x)
            wr = 1-wl
            ig = parent_entropy-(wl*H_s_left+wr*H_s_right)
            
            if ig > best_info_gain + 1e-9:
                best_info_gain = ig
                best_feature_index = c
                best_threshold = x_new[k]

    return (best_feature_index, best_threshold, best_info_gain)
        
            