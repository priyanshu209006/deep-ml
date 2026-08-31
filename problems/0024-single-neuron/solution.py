import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	x = np.array(features)
	w = np.array(weights)
	b = np.array(bias)
	z = np.dot(x,w.T) + b
	sigma = []
	mse = 0
	for i in range(len(x)):
		sigma.append(round(1/(1+np.exp(-z[i])),4))
		mse = mse+(math.pow((sigma[i]-labels[i]),2))/len(x)
	return sigma, mse