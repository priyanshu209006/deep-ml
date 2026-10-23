import numpy as np
def rse(y):
    mean = np.mean(y)
    return np.sum((y - mean)**2)

def threshol(X,y):
    min_mse = rse(y)/len(y)
    feature = None
    threshold = None

    for c in range(X.shape[1]):
        sort_idx = np.argsort(X[:,c])
        x_s = X[:,c][sort_idx]
        y_s = y[sort_idx]
        x_new = []

        for i in range(x_s.shape[0]-1): ##for iterating feature
            if x_s[i] != x_s[i+1]:
                x_new.append((x_s[i]+x_s[i+1])/2)

        for k in range(len(x_new)): ## for iterating each threshold withing each feature
            y_l = y_s[x_s<=x_new[k]]
            y_r = y_s[x_s>x_new[k]]
            rss_l = rse(y_l)
            rss_r = rse(y_r)
            mse_n = (rss_l+rss_r)/len(y)

            if mse_n < min_mse:
                min_mse = mse_n
                feature = c
                threshold = x_new[k]

    return feature, threshold

def tree(X_train,y_train,depth,max_depth,min_samples_split):
    if (len(y_train)<min_samples_split) or (depth>=max_depth) or np.all(y_train==y_train[0]):
        return np.mean(y_train)

    c, threshold = threshol(X_train, y_train)

    if threshold is None:
        return np.mean(y_train)

    left = X_train[:,c]<=threshold
    right = X_train[:,c]>threshold

    return (c,threshold,tree(X_train[left],y_train[left],depth+1,max_depth,min_samples_split),
            tree(X_train[right],y_train[right],depth+1,max_depth,min_samples_split))

def predict(x,tree):
    if not isinstance(tree,tuple):
        return tree

    c,threshold,left_tree,right_tree = tree

    if x[c]<=threshold:
        return predict(x,left_tree)
    else:
        return predict(x,right_tree)

def decision_tree_regressor(X_train,y_train,X_test,max_depth,min_samples_split):
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)

    model = tree(X_train,y_train,0,max_depth,min_samples_split)

    predictions = []
    for x in X_test:
        predictions.append(predict(x,model))
    return np.round(predictions,4).tolist()