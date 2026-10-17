import numpy as np

def multinomial_naive_bayes(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    """
    Implements Multinomial Naive Bayes classifier.

    Args:
        X_train: Training count features (shape: N_train x D)
        y_train: Training labels (shape: N_train)
        X_test: Test count features (shape: N_test x D)
        alpha: Laplace smoothing parameter

    Returns:
        Predicted class labels for X_test (shape: N_test)
    """
    ## Probability of each class
    classes ,counts = np.unique(y_train, return_counts = True)
    pr_c = counts/len(y_train)
    agg = np.array([X_train[y_train == c].sum(axis=0)for c in classes])
    
    D = X_train.shape[1]
    pr_y_c= (agg+alpha)/(np.sum(agg)+D*alpha)
    log_pr = np.log(pr_y_c)


    predicted_class = []
    for x in X_test:
        scores = np.log(pr_c)+x@log_pr.T
        predicted_class.append(classes[np.argmax(scores)])
    return np.array(predicted_class)
