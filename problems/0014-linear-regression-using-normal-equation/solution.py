import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	theta=np.linalg.inv(np.array(X).T@X)@np.array(X).T@y
	return np.round(theta,4)