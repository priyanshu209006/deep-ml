import numpy as np

def gaussian_naive_bayes(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Implements Gaussian Naive Bayes classifier.

    Args:
        X_train: Training features (shape: N_train x D)
        y_train: Training labels (shape: N_train)
        X_test: Test features (shape: N_test x D)

    Returns:
        Predicted class labels for X_test (shape: N_test)
    """

    classes, count = np.unique(y_train, return_counts=True)
    p_c = count / len(y_train)

    mean_feature_each_class = np.array([np.mean(X_train[y_train == c], axis=0) for c in classes])
    variance = np.array([np.var(X_train[y_train == c], axis=0) for c in classes])
    variance = np.maximum(variance, 1e-9)
    ##Suppose:
    #- X_test: 5 test samples, 3 features → (5, 3)
    #- mean_feature_each_class: 2 classes, 3 features → (2, 3)
    #- variance: 2 classes, 3 features → (2, 3)
    log_lik = []
    for i, c in enumerate(classes):
        mean = mean_feature_each_class[i]
        var = variance[i]
        class_likelihood = np.log((1/np.sqrt(2*np.pi*var))*np.exp(-((X_test-mean)**2)/(2*var)))
        log_lik.append(class_likelihood)

    log_lik = np.array(log_lik)
    scores = np.log(p_c[:, None]) + np.sum(log_lik, axis=2)
    pred = classes[np.argmax(scores, axis=0)]
    return pred