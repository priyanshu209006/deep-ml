import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	# Your code here
	n,p = X.shape
	beta = np.array(np.zeros((p+1,1)))
	beta[0] = 0
	loss = []
	X = np.c_[np.ones((n,1)), X]
	for _ in range(iterations):
		z = X@beta
		prob = 1/(1+np.exp(-z))
		del_j = X.T@(prob-y.reshape(n,1))
		loss_value = -(np.dot(y, np.log(prob).flatten())+ np.dot(1 - y,np.log(1 - prob).flatten()))
		loss.append(round(float(loss_value), 4))
		beta = beta- learning_rate*del_j
	beta_list = np.round(beta.flatten(), 4).tolist()
	return beta_list, loss