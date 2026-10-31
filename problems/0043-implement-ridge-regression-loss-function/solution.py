import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	n = X.shape[0]
	# Your code here
	loss  = (1/n)*np.sum((y_true-(X@w.T))**2)+alpha*(np.sum(w**2))
	return loss
