import numpy as np

def make_diagonal(x):
	# Your code here
	n = len(x)
	ar = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i==j:
				ar[i][j] = x[i]
			else:
				ar[i][j] = 0
	return ar